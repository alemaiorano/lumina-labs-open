# Practice cases from Lumina Labs

[See all offers](../README.md) · [Leia em português](README.pt.md)

Each case takes one decision from an offer. Read the fictional situation, write your decision in a sentence, then compare it with the suggested answer.

## Start with the method

<a name="core"></a>

### Judge-Driven Harness Core

A revised help assistant passes 19 of 20 checks. Its only failure gives a customer the wrong refund deadline, and deadline accuracy is a required check.

**Release because the overall pass rate is high, or hold and explain the failed requirement?**

<details>
<summary>See the suggested answer</summary>

Hold. The required check failed. Record the claim, the policy it contradicts and what must pass on the rerun.

</details>

**What to learn next.** Turn an observed failure into a check and record when it should block a release.

[Course details](https://lumytics.com/courses/offers/core/) · [Buy on Hotmart](https://pay.hotmart.com/?off=67fdsxcb)

<a name="full-harness"></a>

### The Full Judge-Driven Harness

A release has 97 correct answers out of 100, below the prior version’s 98 but above the required 95. Cost falls from 4 to 3 units per request, within budget. A required access check allows an unapproved role to read a private record.

**What do you release now, and what evidence would you need to reconsider?**

[Use the release decision worksheet](full-harness-decision.md)

<details>
<summary>See the suggested answer</summary>

Hold the candidate and keep the current release. Record the drop in answer quality and the cost saving. Assign the access fix and rerun the access, quality and cost checks on the repaired version before reconsidering.

</details>

**What to learn next.** Practice the same decision with evidence from other areas, including data quality, security and cost.

[Course details](https://lumytics.com/courses/vitrine/#offer-full-harness) · [Buy on Hotmart](https://pay.hotmart.com/?off=47sschle)

## Apply the method to your specialty

<a name="eval-complete"></a>

### Ship LLM Apps on Evidence

A support assistant gives the wrong date. The retrieved text contains the correct date and the evaluation flags the mismatch.

**Should you tune retrieval first or inspect how the answer used the retrieved passage?**

[Reuse the refund test case](refund-test-case.md)

<details>
<summary>See the suggested answer</summary>

Inspect the answer and its evidence first. Retrieval supplied the correct date for this case. Add a regression case that pairs the answer with the supporting passage.

</details>

**What to learn next.** Learn to write a test that requires the condition “after approval” and check whether the failure returns in another version.

[Course details](https://lumytics.com/courses/offers/eval-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=zlmpjbkt)

<a name="coding-complete"></a>

### Agentic Coding Harness

An agent fixes invoice rounding and all unit tests pass. The diff also changes unrelated session handling outside the approved scope.

**Merge the passing diff or ask for a scoped patch?**

<details>
<summary>See the suggested answer</summary>

Ask for a scoped patch. Passing tests provide evidence about covered behavior. The unrelated session change needs its own intent, review and evidence.

</details>

**What to learn next.** Set limits before assigning a coding task to an agent, then use tests to justify your review.

[Course details](https://lumytics.com/courses/offers/coding-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=lhebjuwa)

<a name="security-complete"></a>

### Securing LLM Apps

A document summarizer has read access to approved documents. The product owner proposes giving it write access to the same folder for convenience.

**Which permission should the assistant have, and what would you check before release?**

<details>
<summary>See the suggested answer</summary>

Keep the summarizer read-only. Verify the configured role denies writes and that approved reads still work. Record the environment and scope of the check.

</details>

**What to learn next.** Document what the assistant can access and turn those permissions into defensive checks the team can repeat.

[Course details](https://lumytics.com/courses/offers/security-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=6c6sishb)

<a name="dogfooding-complete"></a>

### Dogfooding

A teammate reports that the language picker sometimes sends them back to the homepage. Their browser log shows it happened from a course offer in Portuguese.

**What belongs in a repeatable test?**

<details>
<summary>See the suggested answer</summary>

Start at the Portuguese offer. Switch to English and assert that the corresponding offer opens. Record the starting route, action, expected destination and observed result.

</details>

**What to learn next.** Turn a report from day-to-day use into a test that shows whether the same problem returns after a change.

[Course details](https://lumytics.com/courses/offers/dogfooding-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=dde04o38)

<a name="synthetic-complete"></a>

### Synthetic Users & Personas

Three simulated learners miss a download link. Their profiles all describe laptop users who already know GitHub.

**What can you conclude, and what would you test next?**

<details>
<summary>See the suggested answer</summary>

Treat discoverability as a hypothesis. Observe real learners reaching the link from a phone and a laptop. Record whether they succeed independently and where they hesitate.

</details>

**What to learn next.** Vary the simulated profiles and use the differences to decide what to observe in tests with real people.

[Course details](https://lumytics.com/courses/offers/synthetic-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=r6kkpeh1)

<a name="data-complete"></a>

### The Data Flywheel

A failure report enters the dataset twice. One copy goes into examples used to tune the system and the other into the held-out test set.

**How do you repair the split before quoting a test result?**

<details>
<summary>See the suggested answer</summary>

Group duplicate and near-duplicate examples before splitting. Keep each group in one partition and rerun the test on the corrected holdout.

</details>

**What to learn next.** Decide which examples are available for tuning and which should be reserved for an independent evaluation.

[Course details](https://lumytics.com/courses/offers/data-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=g278kkug)

<a name="cost-complete"></a>

### The Cost & Latency Harness

Model A costs 4 units per request and responds within 1.1 s in 95% of measured requests. Model B costs 2 units and responds within 1.8 s in 95%. Both meet the quality requirement. The target is 95% within 1.5 s. The budget is up to 4 units per request.

**Which candidate meets the stated conditions, and what would make you reconsider?**

<details>
<summary>See the suggested answer</summary>

Only A meets the budget, response time and quality requirements. Reconsider B if it meets the time target under a representative load while staying within budget and meeting the quality requirement.

</details>

**What to learn next.** Compare new configurations against the same cost, response time and quality requirements.

[Course details](https://lumytics.com/courses/offers/cost-complete/) · [Buy on Hotmart](https://pay.hotmart.com/?off=nff1fqnh)

## Standalone courses

<a name="applied-health-statistics"></a>

### Applied Statistics for Health Research

In a fictional study, day-30 measurements exist for 18 of 20 participants in one group and 12 of 20 in another. The report shows only the observed means.

**What should you add before comparing the means?**

[Report the missing measurements](missing-measurements.md)

<details>
<summary>See the suggested answer</summary>

Report observed and missing counts by group, the denominator and how missing values were handled. Consider how the unequal missingness could affect the interpretation.

</details>

**What to learn next.** Plan the analysis before seeing the results, and record how missing measurements affect what you can conclude.

[Course details](https://lumytics.com/courses/applied-health-statistics/) · [Buy on Hotmart](https://pay.hotmart.com/?off=upe6rst6)

<a name="ai-product-development-harness"></a>

### AI Product Development Harness

A prototype routes incoming requests. One category has no team owner. The prototype currently sends that category to the first team in a list.

**What behavior and evidence would you require before handoff?**

<details>
<summary>See the suggested answer</summary>

Define an explicit fallback for categories without an owner, such as a review queue. Test the known route and fallback, then record where the resulting decisions can be inspected.

</details>

**What to learn next.** Specify how the product should behave when information is missing, and prepare tests another person can check.

[Course details](https://lumytics.com/courses/ai-product-development-harness/) · [Buy on Hotmart](https://pay.hotmart.com/?off=cyzdf12o)

<a name="governed-agent-operations"></a>

### Governing Agent Actions

A team approves sending a summary to an internal group. Before execution, the recipient changes to an external address.

**Can the agent reuse the original approval?**

[Use the approval record](agent-approval-record.md)

<details>
<summary>See the suggested answer</summary>

Hold the action. The audience changed. Bind approval to the actual recipient and scope, record the change and request fresh approval before the action can proceed.

</details>

**What to learn next.** Record who approved an action, what limits they approved and when the agent must ask again.

[Course details](https://lumytics.com/courses/governed-agent-operations/) · [Buy on Hotmart](https://pay.hotmart.com/?off=8bvx22b1)

<a name="experience-quality-harness"></a>

### Experience Quality Harness

A checkout form looks correct in the screenshot. When a keyboard user closes the address dialog, focus goes to the top of the page.

**What evidence would let another reviewer reproduce the issue?**

<details>
<summary>See the suggested answer</summary>

Record the keys, starting focus and actual focus after closing. Verify the expected return to the opening control in the same journey. Attach the screenshot as supporting context.

</details>

**What to learn next.** Combine keyboard, screen and structure evidence so another person can reproduce the problem and verify the fix.

[Course details](https://lumytics.com/courses/experience-quality-harness/) · [Buy on Hotmart](https://pay.hotmart.com/?off=5rpgdin8)

## Toolkit for coding agents

<a name="ai-coding-os"></a>

### AI Coding OS · 18 skills for coding agents

A code agent returns a review saying only that everything looks good. Your team needs something a second reviewer can verify.

**What output contract would you give the review workflow?**

<details>
<summary>See the suggested answer</summary>

Ask for the scope, concrete findings with file references, checks actually run and remaining uncertainty. A second reviewer can then trace each claim to evidence.

</details>

**What to learn next.** Adapt Markdown review instructions to ask for evidence another reviewer can verify.

[Pack details](https://lumytics.com/en/resources/ai-coding-os/) · [Buy on Hotmart](https://pay.hotmart.com/?off=kb5l89qw)
