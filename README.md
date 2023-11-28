# OpenAI Fine-Tuning Data Preparation

Follow these steps to prepare data for fine-tuning OpenAI models:

## Prerequisites
1. Run the following command to create a JSON file:
   python generate.py

2. Install the required Python packages:
   pip install openai pandas

3. Run the following command to prepare data for fine-tuning:
   openai tools fine_tunes.prepare_data -f prompt_completion_pairs.json
   
- Keep choosing 'y' until it generates a `.jsonl` file.

4. Open Postman and import the provided cURL command.

```bash
curl --location 'https://api.openai.com/v1/files' \
--header 'Authorization: Bearer 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' \
--header 'Cookie: __cf_bm=3EnB.z5ZZmXu8Nlvh6rcXKVo7T26lltbZt_MzMRL4Aw-1701162856-0-AYhFvMYd9/STv+PzbIxT9B1RINTImDOUAmZ7xRAMFLcKrVuNHhDNBQWEVBdmncUavzGD7mYgU6jI+Ptmk6n07YM=; _cfuvid=LN_jpZyjz2S8am7UY2o4HxeVaufaX_Z6XPledwgnU2I-1701161738610-0-604800000' \
--form 'purpose="fine-tune"' \
--form 'file=@"path to your .jsonl"'


In the "Body" tab, select purpose as the key and fine-tune as the value.
Select file as the key and choose 'Select Files' as the value.
Open the "Authorization" tab in Postman. Choose the type as "Bearer Token" and enter your OpenAI API key as the token value.

Hit the API.

After hitting the API, check your OpenAI account at OpenAI Platform Files to ensure that the files are uploaded successfully.