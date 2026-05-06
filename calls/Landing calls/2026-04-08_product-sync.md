# Product Sync

**Date:** 2026-04-08
**Duration:** 41 minutes
**Participants:** Anna Irving (product manager), Roman Carter (product designer), Stan Oliver (data analyst)

## Transcript

[00:00]

**Anna:**
Hey guys. Roman, you there?

**Roman:**
Yeah, hey. Just grabbing some coffee, one sec.

**Stan:**
Hey. I'm ready.

**Anna:**
Ok, while Roman's grabbing his coffee — some context. Tony messaged me yesterday saying we need to urgently update the website. He says sales is losing deals because the site has outdated or inaccurate info. Let's go through what's actually working in the product so I can give marketing the current data.

**Roman:**
Finally. I've been saying for six months that our site doesn't match the product.

**Stan:**
Agreed.

[02:15]

**Anna:**
Let's go in order. I'll list what's actually in prod, no marketing fluff. First — the attrition prediction model, 84% accuracy over a 90-day horizon. Second — the burnout model, it's new, been running for six months, 79% accuracy but it's improving every month. Third — the recommendation engine: for each employee in the red zone the system generates 3 to 5 specific actions — transfer, salary review, conversation with their manager, workload adjustment. Fourth — the "team heatmap": a manager sees their department and gets a real-time read on the overall state. Fifth — integrations: NetSuite, SAP HR, Workday, Slack, corporate email. That's what's in prod. Stan, did I miss anything?

**Stan:**
No, that's all right. Although on the burnout model — I'd clarify that 79% is on the current dataset. With clients who have good data it gets up to 83%.

**Anna:**
Ok, but for the site let's go with 79% — that's the honest average.

**Stan:**
Agreed.

[05:30]

**Roman:**
Anna, I just looked at what we have on the site right now. It literally says — "next-generation HR analytics: dashboards and predictions." That's... well, that's like selling a Tesla and writing "a wheeled vehicle."

**Anna:**
Yeah, Marina wrote that copy before we shipped the recommendation engine. She hasn't updated it since.

**Stan:**
Speaking of Marina. She messaged me yesterday, asked me for a "nice number about predictions." I explained — we don't predict WHO will quit. We identify the risk zone. That's a fundamental difference.

**Anna:**
Spell it out for the record.

[07:45]

**Stan:**
We're saying: "These 40 people out of 2,000 are in the red zone. With 84% probability at least 34 of them will leave within the next 90 days if nothing is done." We're not pointing a finger at a specific person. That's important for ethics and for GDPR. Marina apparently didn't grasp the difference and wrote something on the site like "find out which of your employees is planning to quit." That's... wrong. And legally risky.

**Roman:**
Oh god. Seriously?

**Stan:**
Seriously. If a client takes that literally and starts firing people based on our forecast — we've got a legal scandal on our hands. The model works with groups and risk zones, not individual people.

**Anna:**
Stan, can you drop me the exact wording in Slack — how to describe it correctly? I'll pass it to marketing.

**Stan:**
Sure. I'll write it up after the sync.

[10:20]

**Anna:**
Good. Now let's talk metrics. Stan, what's the headline number we can use?

**Stan:**
The headline number — clients who follow the system's recommendations reduce turnover by an average of 34% in the first 6 months.

**Anna:**
34 percent! That's a killer number for the landing page. I don't understand why the site says "improve your HR team's efficiency." What efficiency? Minus 34% turnover — that's what we should be writing.

**Roman:**
Wait, 34% — is that across all clients? Or a select group?

**Stan:**
That's the average across 52 clients who've been using the product for more than 6 months and are actively applying the recommendations. For those who don't follow the recommendations — it's around 12% reduction, just from awareness alone.

**Anna:**
So even without recommendations — minus 12%. And with recommendations — minus 34%. Both numbers are good.

**Stan:**
Yeah, but 34% is when the HR director actually executes the recommendations. Redistributes workload, has conversations, revisits conditions. Not everyone does that.

[13:00]

**Roman:**
By the way, I wanted to bring something up. You know what clients screenshot most from our product and send to their leadership?

**Anna:**
The dashboard?

**Roman:**
No! Not the dashboard, not the forecast. It's the "Risk Factors" screen. For each red zone it shows WHY people are leaving: overwork — 42%, below-market pay — 38%, no career growth — 27%, conflict with manager — 19%. And those percentages are real, specific to that company, not industry averages.

**Anna:**
How do you know they're screenshotting it?

**Roman:**
We have click analytics. The "Risk Factors" screen is the most visited. Average time on screen — 4 minutes, that's three times more than on the dashboard. And I've personally watched clients at demos immediately get glued to this screen.

[15:30]

**Stan:**
Roman's right. An HR director goes to the CEO and says: "The problem isn't salaries — it's three department heads creating a toxic environment. Here's the data." That's our killer feature, and there's not a word about it anywhere on the site.

**Anna:**
Guys, this is insane. We've got the most valuable screen in the product — and it's not even mentioned on the site. Roman, can you do a screenshot of that screen? I need it for marketing.

**Roman:**
On demo data? Of course. I can even record a video — opening it, drilling down to a specific department.

**Anna:**
Let's have the video too. And the screenshot. Marketing needs visual proof, not just copy.

[18:00]

**Roman:**
One more thing. I ran a usability test with new clients. You know what confuses them on the site?

**Anna:**
What?

**Roman:**
The word "analytics." They come in expecting another BI tool. Then they're surprised: "Oh, you also give recommendations?" I think we need to change the positioning. This isn't analytics, it's a management system.

**Stan:**
Paul Crawford said the same thing yesterday at the strategy session, by the way.

**Anna:**
I know, I was at the strategy session. But that's a separate conversation.

[20:15]

**Anna:**
Alright, let's go through integrations. Stan, what's the status on NetSuite?

**Stan:**
NetSuite — full two-way integration. Onboarding takes 3 days if the client has a standard configuration. Non-standard — up to 5 days, but we rarely see that.

**Anna:**
SAP?

**Stan:**
SAP HR — connector is ready, running stable. Onboarding — 4 days. One nuance — we need API access on the client side, which sometimes takes time with their security team.

**Roman:**
Workday and Slack — automated notifications. Configured in an hour. Email is also quick.

**Anna:**
Good. All of this needs to be on the site as a list with logos. Kevin from sales says every other client asks about NetSuite.

[23:00]

**Roman:**
Oh, I also wanted to mention. Remember we talked about the mobile version of the heatmap?

**Anna:**
Yeah, what's going on with it?

**Roman:**
It works. I finished it last week. An HR director can open their phone in the morning and in 30 seconds see which departments are in the green, yellow, and red zone. No logging into a laptop, no opening a dashboard.

**Stan:**
What about push notifications?

**Roman:**
Those work too. If someone moves into the red zone — a push comes through. We haven't rolled it out broadly yet, but on the beta with three clients — working great.

**Anna:**
That needs to be on the site too. A mobile notification on Monday morning — that's exactly what Tony from sales is asking for.

[26:30]

**Stan:**
Hey, what if I put together a doc with all the current metrics? Because some of the data on the site is six months old.

**Anna:**
Yeah, let's do it. But with sources — where each number comes from and what dataset it's based on. So marketing doesn't just make things up.

**Stan:**
Sure. I can have it by Friday.

**Roman:**
Stan, include the trial-to-paid conversion rate. It's strong — 68%, if I remember right.

**Stan:**
67%, but yeah, that's a good number. I'll include it.

[28:45]

**Anna:**
Ok, let's get back to action items. Roman, you're doing screenshots and video of the "Risk Factors" screen — when?

**Roman:**
Tomorrow. I need fresh demo data. Stan, can you throw some together?

**Stan:**
Yeah, I'll load it tonight. I'll make a realistic scenario — company of 1,500 people, broken down by department.

**Anna:**
Great. Stan — metrics doc by Friday. Roman — visuals by Wednesday. I'll be pulling everything together and putting together a brief for marketing. Tony wants to see an updated site in two weeks, so let's not drag our feet.

[31:00]

**Roman:**
Two weeks is very optimistic. Marketing usually takes a month to do anything.

**Anna:**
Tony said "two weeks" — so we're pushing. I don't want to be stuck between him and marketing.

**Stan:**
Fair enough.

**Roman:**
Alright. Oh, one more small thing — we should update the demo environment. Right now demos are showing the old interface, the one before the redesign. Clients see one thing on the demo, then something different in prod. It's confusing.

**Anna:**
Agreed. Adding it to the task list. Roman, can you update the demo environment in parallel with the visuals?

**Roman:**
I'll try. But if I run out of time — visuals take priority.

**Anna:**
Ok.

[33:30]

**Stan:**
Anna, one more question. The site says the model was trained "on millions of records." I'd take that out. The actual number is 847,000 records over two years. That's a solid dataset, but "millions" is a lie. If a journalist or client checks — it'll be embarrassing.

**Anna:**
Wow. I didn't know that's what the site said. Thanks, I'll add it to the list of fixes.

**Roman:**
Marina loves to round up.

**Anna:**
Ok, let's skip the commentary on Marina. We'll just fix it.

[35:15]

**Stan:**
Last thing from me. On the burnout model — we're shipping an update next week. Accuracy should go up to 82-83%. I added new factors: overtime frequency, response patterns in company surveys, changes in activity in work messengers. The data is anonymized, of course.

**Anna:**
Good, but let's not put 83% on the site yet — let's wait until it's confirmed on client data.

**Stan:**
Agreed. A month or two.

[37:00]

**Roman:**
Anna, on the demo video — Tony's asking for a 90-second video for the site. Want me to record a rough cut? I can do a screen capture with voiceover.

**Anna:**
That'd be great. Just no marketing language — show the product as it is. Make it "here's what a morning check looks like for an HR director." Simple scenario, real.

**Roman:**
Got it. I'll record it this week on demo data.

**Stan:**
If you need help with the numbers for the demo — just say the word.

**Roman:**
Will do.

[39:00]

**Anna:**
Ok, summary. Stan — metrics by Friday, correct wording on risk zones today. Roman — visuals by Wednesday, demo video by Friday, demo environment update if you have time. Me — brief for marketing, pulling everything into one doc. Questions?

**Roman:**
Nope.

**Stan:**
No, all clear.

**Anna:**
Great, thanks everyone. Have a good day.

**Roman:**
Bye!

**Stan:**
Bye.
