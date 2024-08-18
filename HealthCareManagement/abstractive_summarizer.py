from transformers import BartForConditionalGeneration, BartTokenizer

class AbstractiveSummarizer:

    def _init_(self):
        return
    
    def generate_summary(self, sentences):
        # Load the BART model and tokenizer

        model_name = "facebook/bart-large-cnn"
        model = BartForConditionalGeneration.from_pretrained(model_name)
        tokenizer = BartTokenizer.from_pretrained(model_name)

        # Tokenize and summarize the user input

        inputs = tokenizer.encode("summarize: " + sentences, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode and print the summary
        
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print(summary)
        return summary
