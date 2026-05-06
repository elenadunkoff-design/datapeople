# Product Team Standup

**Date:** 2026-03-07
**Duration:** 18 minutes
**Participants:** Kevin Larson (Head of Product), Adam Vasquez (Developer), Natalie Cruz (Developer), Mike Peters (Developer)

## Transcript

**Kevin Larson:**
Okay, hey everyone. Let's do a quick rundown. Adam, you're up.

**Adam Vasquez:**
Hey. I spent all day yesterday wrestling with a problem in the Workday connection. Remember, a client complained that employee data wasn't syncing between our system and theirs?

**Kevin Larson:**
Yeah, that one's been sitting for a week now?

**Adam Vasquez:**
Yep. So, it's more complicated than we thought. Workday changed how they send data back to us, and when there are a lot of employees, the sync just breaks. I need to rewrite the whole piece that handles it. It's not a couple of hours, it's two or three days.

**Kevin Larson:**
Two or three days? Our two-week work cycle ends Friday.

**Adam Vasquez:**
I know. But if we slap a bandaid on it now, it'll be even worse later. It really needs to be done properly.

**Kevin Larson:**
Alright, let's talk after standup. Maybe we can break it into chunks. Natalie?

**Natalie Cruz:**
I'm on track, finishing the notification settings page. Should close it out today, goes for someone else to review my code tomorrow.

**Kevin Larson:**
Great.

**Natalie Cruz:**
But I have a question. Someone from marketing wrote me, Elena. They want us to build a landing page for the new pricing plan. They're saying the current one isn't working well — not enough people are submitting requests.

**Kevin Larson:**
A landing page? That's not even our task, marketing should be handling that.

**Natalie Cruz:**
Well, they say they need help with the front-end part, and that it's "quick, just a couple of sections to change."

**Kevin Larson:**
Natalie, that's not in our plan for this cycle. Have Elena log a request, and we'll look at it in the next planning session. Our priorities are set right now.

**Natalie Cruz:**
Okay, I'll tell her that. It's just that she's asked three times already.

**Kevin Larson:**
I get it, but we can't take on tasks out of thin air in the middle of a cycle. Mike?

**Mike Peters:**
Hey. I finished speeding up the database lookups for the analytics dashboard yesterday. Noticeably faster now, from seven seconds down to one and a half.

**Kevin Larson:**
Nice, good work.

**Mike Peters:**
Thanks. But I wanted to bring up the old messy code situation. The reports section — that's code from when we first launched, a year and a half ago. Only about twenty percent of it has proper checks to make sure changes don't break things. Every time I go in there, I'm scared I'll break something.

**Kevin Larson:**
Mike, I agree it's a problem. But every week it's the same story: let's clean up the old code, and then something urgent lands on us.

**Mike Peters:**
Right, exactly. Can we at least dedicate twenty percent of our time to it? Consistently.

**Kevin Larson:**
Let me bring it up at the team review. I need to discuss it with Dave.

**Kevin Larson:**
Alright, anything blocking you guys?

**Adam Vasquez:**
I need access to that client's Workday test account. Kevin, can you ask support?

**Kevin Larson:**
Yeah, I'll message them after the call. Okay, that's it. Adam, hang back — let's talk about the sync issue.
