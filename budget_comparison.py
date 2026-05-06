import json
import subprocess
import sys

SPREADSHEET_ID = "1SvzXmgF1MWmmaSTjHt-HsgDwYCtEEg2szw39koxcxmo"
MONTHS = ["July", "August", "September", "October", "November", "December"]


def gws_get(range_name):
    result = subprocess.run(
        [
            "gws", "sheets", "spreadsheets", "values", "get",
            "--params", json.dumps({"spreadsheetId": SPREADSHEET_ID, "range": range_name}),
        ],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)["values"]


def parse_dollars(s):
    return float(s.replace("$", "").replace(",", ""))


# --- Read data ---
plan_rows = gws_get("Plan")
actual_rows = gws_get("Actual")

# Plan: find the "Total" row
plan_header = plan_rows[0]
month_indices = {m: plan_header.index(m) for m in MONTHS}

plan_total_row = next(r for r in plan_rows if r[0] == "Total")
plan_totals = {m: parse_dollars(plan_total_row[month_indices[m]]) for m in MONTHS}
plan_grand_total = sum(plan_totals.values())

# Actual: single data row
actual_header = actual_rows[0]
actual_data_row = actual_rows[1]
actual_totals = {m: parse_dollars(actual_data_row[actual_header.index(m)]) for m in MONTHS}
actual_grand_total = sum(actual_totals.values())

# --- Compute comparison ---
rows = []
rows.append(["Month", "Plan ($)", "Actual ($)", "Variance ($)", "Variance (%)"])

total_variance_dollars = 0
for month in MONTHS:
    plan = plan_totals[month]
    actual = actual_totals[month]
    variance_dollars = actual - plan
    variance_pct = (variance_dollars / plan) * 100
    total_variance_dollars += variance_dollars
    rows.append([
        month,
        f"${plan:,.2f}",
        f"${actual:,.2f}",
        f"${variance_dollars:,.2f}",
        f"{variance_pct:.1f}%",
    ])

total_variance_pct = (total_variance_dollars / plan_grand_total) * 100
rows.append([
    "TOTAL",
    f"${plan_grand_total:,.2f}",
    f"${actual_grand_total:,.2f}",
    f"${total_variance_dollars:,.2f}",
    f"{total_variance_pct:.1f}%",
])

# --- Print results ---
print("\n=== Budget Comparison ===")
for row in rows:
    print("  ".join(str(c).ljust(18) for c in row))

# --- Write to Comparison tab ---
# First, try to clear/create the sheet
# Check if Comparison sheet exists
meta = subprocess.run(
    ["gws", "sheets", "spreadsheets", "get",
     "--params", json.dumps({"spreadsheetId": SPREADSHEET_ID})],
    capture_output=True, text=True
)
meta_json = json.loads(meta.stdout)
sheet_names = [s["properties"]["title"] for s in meta_json["sheets"]]

if "Comparison" not in sheet_names:
    # Add the sheet
    subprocess.run(
        ["gws", "sheets", "spreadsheets", "batchUpdate",
         "--params", json.dumps({"spreadsheetId": SPREADSHEET_ID}),
         "--json", json.dumps({"requests": [{"addSheet": {"properties": {"title": "Comparison"}}}]})],
        capture_output=True, text=True
    )
    print("\nCreated 'Comparison' tab.")
else:
    # Clear it
    subprocess.run(
        ["gws", "sheets", "spreadsheets", "values", "clear",
         "--params", json.dumps({"spreadsheetId": SPREADSHEET_ID, "range": "Comparison"}),
         "--json", "{}"],
        capture_output=True, text=True
    )
    print("\nCleared existing 'Comparison' tab.")

# Write data
write_result = subprocess.run(
    ["gws", "sheets", "spreadsheets", "values", "update",
     "--params", json.dumps({
         "spreadsheetId": SPREADSHEET_ID,
         "range": "Comparison!A1",
         "valueInputOption": "USER_ENTERED",
     }),
     "--json", json.dumps({"values": rows})],
    capture_output=True, text=True
)

if write_result.returncode == 0:
    print("Written to 'Comparison' tab successfully.")
else:
    print("Error writing:", write_result.stderr)
