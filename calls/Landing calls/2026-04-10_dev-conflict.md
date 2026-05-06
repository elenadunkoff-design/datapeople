# Conversation with the Tech Lead + Debrief

**Date:** 2026-04-10
**Duration:** 22 minutes (two conversations: Tony + Dave — 11 minutes, then Tony + Elena — 11 minutes)
**Participants:** Tony Grant (Head of Sales), Dave Kowalski (CTO) — Part 1; Tony Grant, Elena Meyers (Sales Manager) — Part 2

## Transcript — Part 1: Tony + Dave

[00:00]

**Tony:**
Dave, got a minute?

**Dave:**
No. I've got a code review burning and a release on Thursday.

**Tony:**
One minute, Dave.

**Dave:**
Fine. One.

**Tony:**
The website says "implementation from 3 months." Is that true?

**Dave:**
No. That was true six months ago.

**Tony:**
So what's the number now?

**Dave:**
Depends on the client.

**Tony:**
Dave.

**Dave:**
What, "Dave"?

**Tony:**
I need a real number. Not "depends on the client." A real number I can tell a client and it'll actually be true.

[01:30]

**Dave:**
Tony, stop bugging me about this landing page. I'll tell you one thing and then leave me alone. Implementation takes 2 weeks, not 3 months like it says on the site. We rewrote the integration module last quarter.

**Tony:**
Two weeks. You sure?

**Dave:**
Yes. If the client's on NetSuite or SAP — data connection is 3 days. Model setup — a week. Calibration — another 3-4 days. Two weeks and the system's delivering its first predictions. Used to be 2-3 months when we were doing field mapping by hand. Now it's automatic.

**Tony:**
What if the client's not on NetSuite or SAP?

**Dave:**
Custom HR system — longer. Could be a month. But that's maybe 10-15% of clients. Everyone else is on NetSuite or SAP.

[03:15]

**Tony:**
The website's had "3 months" up there for two months. Dave, do you get that I've been losing deals because of this?

**Dave:**
Tony, I'm not in marketing. I did my job — rewrote the module, made implementation 6x faster. The fact that Marina didn't update the site is not my problem.

**Tony:**
Then whose is it?

**Dave:**
Marina's. Or yours — you could've come and asked sooner.

**Tony:**
I did ask! A month ago I asked Marina "are the timelines on the site current?" and she said "yes, three months, I checked with Dave."

**Dave:**
She didn't check with me. Last time Marina messaged me was January. About a logo for a slide.

**Tony:**
...

[05:00]

**Dave:**
Look, I don't want to get into all that. I gave you the number — 2 weeks for standard integrations. Write "2 weeks to first results" on the site and stop calling me.

**Tony:**
What if a client asks for details?

**Dave:**
What details? Data connection — 3 days. We take an export from their HR system and map it to our data model. Used to be an engineer doing it manually — sitting there matching fields, writing converters. Now it's automatic mapping. I wrote a neural field classifier. It figures out in about an hour where the client has name, job title, salary, tenure. Works on 94% of fields automatically, the rest is a couple hours of manual review.

**Tony:**
That's actually impressive. Automatic mapping — that's something you can sell.

**Dave:**
It's not a feature, it's infrastructure. Don't sell it. The client doesn't care how we map the data. What matters to them is that they're seeing results in 2 weeks.

[07:30]

**Tony:**
Okay. What about load — if it's a big client, 10,000 employees? Does it hold up?

**Dave:**
It holds up. NovaPower Corp — 12,000, we handle it fine. Tested up to 25,000 — also fine. Past 15,000 the model calculations run overnight, results are ready in the morning. Transparent to the client.

**Tony:**
Good. Thanks.

**Dave:**
That it? Can I go?

**Tony:**
Wait, one more thing. ROI calculator on the site — can you do it?

**Dave:**
A calculator's frontend work. 3-4 days if the formulas are ready. Ask Stan for the formulas, then come back.

**Tony:**
When can you pick it up?

**Dave:**
After the release. Next week. If nobody piles on more tasks.

[09:30]

**Tony:**
Paul said he'd talk to you. It's a priority.

**Dave:**
If Paul says so — I'll do it. Not when you say so.

**Tony:**
Dave, we're on the same team.

**Dave:**
Tony, we're on the same team, but I've got 14 tasks in the sprint and 6 developers, one of whom is out sick and another is a junior who needs everything explained twice. I'm not against the calculator. I'm against someone showing up every day with a "urgent" task. Set the priorities — I'll get it done.

**Tony:**
Fair enough. Sorry.

**Dave:**
Ok. I'm out. Later.

**Tony:**
Later, Dave.

---

## Transcript — Part 2: Tony + Elena (immediately after)

[11:00]

**Tony:**
Elena, you around?

**Elena:**
Yeah, what's up?

**Tony:**
I just came from Dave. You know what I found out?

**Elena:**
What?

**Tony:**
Implementation — two weeks. Not three months. Two. Weeks.

**Elena:**
You're kidding.

**Tony:**
I'm not. They rewrote the integration module. Automatic data mapping, the whole thing. NetSuite or SAP — connection in 3 days. A week for models. 3-4 days calibration. Total — 2 weeks to first predictions.

[12:30]

**Elena:**
Tony... I lost SteelVault Group partly because of this. They told me straight to my face: "Three months — we can't wait that long, we've got a budget for this quarter, we need results before summer."

**Tony:**
I know. And I lost PetroMax for the same reason.

**Elena:**
What about MegaMart?

**Tony:**
MegaMart too. Their CTO said: "In three months we'll build something ourselves."

**Elena:**
God. That's... how much money did we lose?

**Tony:**
I'm counting three deals. Minimum. SteelVault — $980,000 annual contract. PetroMax — about the same. MegaMart — $600,000. That's almost $2.6 million a year. Because the site says "3 months" instead of "2 weeks."

[14:15]

**Elena:**
I'm in shock. Did Marina know?

**Tony:**
See? Two months the site's had "implementation from 3 months." I lost three deals because clients were reading that and saying "Three months is too long, we want faster." And the real answer is two weeks. Marina! Fine, I'll handle it myself...

**Elena:**
Handle what yourself?

**Tony:**
I'll fix it myself. I'll go to Paul if I have to. But this needs to be on the site tomorrow. Not in a month, not in a week — tomorrow.

[15:45]

**Elena:**
How was Dave, anyway? Was he pissed?

**Tony:**
Dave's always pissed. But he's right on the substance — he did his job, made implementation 6x faster. It's marketing that didn't update the information.

**Elena:**
You know, maybe we should put together a list ourselves of everything that's wrong on the site? Go through every point — what it says and what it should say?

**Tony:**
Good idea. Let's do it.

**Elena:**
Okay, off the top of my head. "Implementation from 3 months" — should be "2 weeks." "50-70 clients" — should be 78. "HR analytics" — Paul wants "human capital management system."

[17:30]

**Tony:**
"We predict who's going to quit" — Stan says that's just wrong. We identify risk zones for groups, we don't point the finger at a specific person. It's a legally risky way to put it.

**Elena:**
Wow, I didn't know that.

**Tony:**
Neither did I until yesterday. Anna said at the strategy session that the site has zero case studies with numbers, no ROI, no integration list, and our main metric is missing — minus 34% turnover in six months.

**Elena:**
34%?

**Tony:**
Yeah. Clients who follow the system's recommendations reduce turnover by 34% in the first 6 months. That's a killer number. It's not on the site.

[19:15]

**Elena:**
You know what hurts? If the site had real data, I wouldn't have to improvise at every meeting. I'd just open the site and show them.

**Tony:**
Exactly. The site should be working for us, not against us. Right now it's working against us.

**Elena:**
So what's the timeline? When does everything get updated?

**Tony:**
Paul said — this month. Anna's coordinating. I'll be pushing.

**Elena:**
Alright. I've got to jump on a call with TelecomOne. Wish me luck.

[20:30]

**Tony:**
Good luck. And hey — when you talk about implementation, say "2 weeks to first results." Don't look at the site. The site'll get fixed.

**Elena:**
What if they go to the site and see "3 months"?

**Tony:**
Say: "The information on the site is outdated, we're updating it this week. The real timeline is 2 weeks — I can confirm that in writing." If you need me, I can jump on the call.

**Elena:**
Ok, thanks. Gotta run.

**Tony:**
Go. Tell me how it went after.

**Elena:**
Definitely. Bye!

**Tony:**
Bye.
