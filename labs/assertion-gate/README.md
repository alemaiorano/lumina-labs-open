# One unsupported deadline holds a release

Compare two refund answers against the same policy. Correct the unsupported number and check the decision again.

## Run

```sh
python3 assertion_gate.py
```

The default run exits 0 for inspection. Add `--ci` when the failed assertion should return exit code 1.

The input uses one JSON object per line. Use a nonempty claim and source, the rubric `groundedness` and a numerical threshold from 0 to 1. An answer with zero matching words always fails.

## Expected output

```text
id       score   bar  verdict  evidence
------------------------------------------------------------------------------
refund-5d  1.00  0.80  PASS     rubric=groundedness; supported=5,business,days,processed,refunds; missing=<none>
refund-14d  0.80  0.90  FAIL     rubric=groundedness; supported=business,days,processed,refunds; missing=14

release gate: 1/2 assertions passed -> HOLD
claim + source + rubric + threshold = an assertion that can fail
```

## What to change

Change only the number `14` in the failing claim to `5`. The notebook makes this change in a temporary copy. Run the check again and explain what changed in the evidence.

[Notebook](assertion-gate.ipynb)

## How to interpret

The score measures word overlap on this fixture. A match can miss negation or the condition **after approval**. The numbers and scores are synthetic and illustrate the exercise.

[MIT](../../LICENSE)
