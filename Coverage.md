Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src\__init__.py          0      0   100%
src\order_io.py         22      2    91%   13, 17
src\pricing.py          33      0   100%
--------------------------------------------------
TOTAL                   55      2    96%

The only uncovered lines are in `src/order_io.py` (lines 13 and 17).  
Those lines handle simple CSV parsing logic — splitting and trimming each `name,price` entry.  
Because the integration test already supplies well-formed order data, these branches are low risk and do not impact correctness.  
All functional code paths (discount, tax, bulk totals, formatting, and I/O) are otherwise fully exercised by the test suite.
