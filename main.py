import openai
openai.api_key = "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" #Use your own api key

openai.fine_tuning.jobs.create(
  training_file="prompt_completion_pairs_prepared.jsonl", 
  model="gpt-3.5-turbo"
)