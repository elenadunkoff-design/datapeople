# Skill: /video-hosting-publish

Read approved rows from the Google Sheet and publish each video to the hosting API.

---

## Config

- Sheet ID: `12jd1KZ_wDrLNtalcMPcq5JXhc8KxlbHWEF83-bSdBL0`
- Tab: `Sheet1`
- API endpoint: `POST https://agentsim.pro/video_hosting/api/videos`
- Bearer token: `vh_56bf23f42af73fd098f3c2e40366161f844548f7`
- Videos folder: `~/datapeople/DataPeople — Module 5 inputs (EN)/videos/`

## Sheet column layout

- A: Video File
- B: Title 1 | C: Description 1 | D: Thumbnail 1
- E: Title 2 | F: Description 2 | G: Thumbnail 2
- H: Title 3 | I: Description 3 | J: Thumbnail 3
- K: Approved Title | L: Approved Description | M: Approved Thumbnail
- N: Status

---

## Steps

### 1. Read the sheet

Use `gws sheets spreadsheets values get` to read all rows from `Sheet1`.

### 2. Find approved rows

Filter for rows where column N (Status) = `approved` (case-insensitive).

If no approved rows are found, report "No approved rows found — nothing to publish." and stop.

### 3. For each approved row

**a) Validate**

Check that the following are non-empty before attempting to publish:
- Column A (Video File)
- Column K (Approved Title)
- Column L (Approved Description)
- Column M (Approved Thumbnail)

If any are missing, skip the row and report a warning: `Row {n} skipped — missing: {field list}`.

**b) Locate files**

- Video: `~/datapeople/DataPeople — Module 5 inputs (EN)/videos/{Video File}`
- Thumbnail: the path stored in column M (Approved Thumbnail)

Verify both files exist before posting. If either is missing, skip the row with a warning.

**c) POST to the API**

Send a `multipart/form-data` POST request using `curl`:

```bash
curl -s -X POST https://agentsim.pro/video_hosting/api/videos \
  -H "Authorization: Bearer vh_56bf23f42af73fd098f3c2e40366161f844548f7" \
  -F "title={Approved Title}" \
  -F "description={Approved Description}" \
  -F "video=@{absolute video path}" \
  -F "thumbnail=@{absolute thumbnail path}"
```

Capture the response. A successful response will contain an `id` or `status: success` field.

**d) Handle the response**

- On success: proceed to update the sheet.
- On failure (non-2xx HTTP code or error in response body): log the error, skip the status update for that row, and continue to the next row. Do not mark failed rows as published.

**e) Update the sheet**

For successfully published rows, update column N to `published`.

Use `gws sheets spreadsheets values update` targeting the exact cell (e.g. `Sheet1!N3`) with `valueInputOption: USER_ENTERED`.

### 4. Report

After processing all approved rows, print:

```
Published: {n} video(s)
Skipped:   {n} (with reasons)
Failed:    {n} (with error details)
```

List each published video by filename and the API response ID if available.
