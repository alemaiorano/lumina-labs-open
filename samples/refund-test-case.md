# Test a refund answer

[Back to the exercises](README.md#eval-complete) · [Leia em português](refund-test-case.pt.md)

**Fictional policy.** Refunds are processed within 5 business days after approval.

**AI answer.** “Refunds are processed within 14 business days.”

Rewrite the answer and use the worksheet to decide which versions a check should accept. Fill it in on paper or copy it into your team’s test notes.

| Field | Your test case |
| --- | --- |
| Question asked of the AI | |
| Policy excerpt that supports the answer | |
| Number and unit the answer must preserve | |
| Condition the answer must mention | |
| Example answer that should pass | |
| Example answer that should fail | |

<details>
<summary>Compare with the suggested answer</summary>

The answer **“The refund is processed within 5 business days after approval”** preserves the deadline and when it starts. Test two separate failures: **14 business days after approval** and **5 business days** without saying that the deadline starts after approval. That way, a version that fixes the number while omitting the condition still fails your test.

</details>

To run the example and compare the results, use the [JSONL test cases](../labs/assertion-gate/samples/claims.jsonl) and the [lab instructions](../labs/assertion-gate/README.md). The supplied code checks for matching words. You can add the condition above to your own test.

**What to learn next.** Write a check for the condition “after approval” and use the same case to see whether the error returns in a later version. [Explore the AI Evaluations course](https://lumytics.com/courses/offers/eval-complete/).
