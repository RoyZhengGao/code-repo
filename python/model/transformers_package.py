from transformers import *
import torch
from torch.nn.functional import softmax

# if you have your tokenizer / model saved in local, you can specify your path. Otherwise 
# it will automatically use this path to download form Amazon S3
pretrained = 'albert_chinese_tiny' 
# tokenizer = BertTokenizer.from_pretrained(pretrained)
# model = AlbertForMaskedLM.from_pretrained(pretrained)
tokenizer = BertTokenizer.from_pretrained("clue/roberta_chinese_base")
model = BertModel.from_pretrained("clue/roberta_chinese_base")

# that is how you save the tokenizer
tokenizer.save_pretrained("./roberta_chinese_base") 

# that is how you save the language model, 
#need to create a folder beforehand.

model.save_pretrained("./roberta_chinese_base") 
# inputtext = "今天[MASK]情很好"

# maskpos = tokenizer.encode(inputtext, add_special_tokens=True).index(103)

# input_ids = torch.tensor(tokenizer.encode(inputtext, add_special_tokens=True)).unsqueeze(0)  # Batch size 1
# outputs = model(input_ids, masked_lm_labels=input_ids)
# loss, prediction_scores = outputs[:2]
# logit_prob = softmax(prediction_scores[0, maskpos]).data.tolist()
# predicted_index = torch.argmax(prediction_scores[0, maskpos]).item()
# predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
# print(predicted_token,logit_prob[predicted_index])