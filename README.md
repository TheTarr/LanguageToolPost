# LanguageToolPost

## Files

wiki_util.py

- Generate a txt of wiki pure text, start crawing from "Neural networks".

proof_read_wiki_txt.py

- Read the txt file generated by wiki_util, print the modification from LanguageTool as box attached to original text.

json_processor.py

- Generate original sentences from W&I dataset json file (filtered, only sample length < 1300).

ground_truth_process.py

- Generate modified sentences from W&I dataset json file.

ground_truth_check.py

- Generate modified sentences by LanguageTool from W&I dataset json file.

lang8.py

- Generate original sentences, modified sentences and modified sentences by LanguageTool from Lang-8 dataset, English.
