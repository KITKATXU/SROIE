### Rule1

> Delete duplicated TOTAL values in one invoice.

### Rule2

> Label the digits tokens right before and after 'S-TOTAL' tokens as  'S-TOTAL'.

### Rule3

> For the invoices without a TOTAL value, find the last cash token and label the proceeding digits tokens as  'S-TOTAL'.

### Rule4

> For the invoices without a TOTAL value, find the last total token and label the succeeding digits tokens as  'S-TOTAL'.

### Rule5

> For the invoices without a TOTAL value, sort all float tokens and label the maximum one as 'S-TOTAL'.

### Rule6

> For the invoices without a DATE value, match their tokens with patterns like 'X/X/X' or 'X-X-X'.

### Rule7

> For the invoices without a TOTAL value, select all digits tokens and simply label the last 4 as 'S-TOTAL'.


