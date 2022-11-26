# layoutlm-finetuned-sroie

This model is a fine-tuned version of [microsoft/layoutlm-base-uncased](https://huggingface.co/microsoft/layoutlm-base-uncased) on the sroie dataset.

I used KFold to split the data and trained 5 models. Before that,  the data are shuffled based on their invoice number.

The probability results of each token provided by the 5 models are simply stacked by summing up.  For those with high scores on 'S-TOTAL', they are classified as 'S-TOTAL', even if the scores are lower than 'O'.

The f1 score on op-test dataset based on my model are 88.04.

To improve my results, 7 manually built rules are applied. The final f1 reached 92.83.

See rule introductions in directory rules.

