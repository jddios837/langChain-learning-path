from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

qs = ["Which NFL team won the Super Bowl in the 2010 season?",
      "If I am 6 ft 4 inches, how tall am I in centimeters?",
      "Who was the 12th person on the moon?",
      "How many eyes does a blade of grass have?"
      ]

print(llm.get_num_tokens("Hola a todos"))

llm_result = llm.generate(qs)
print(len(llm_result.generations))

for x in llm_result.generations:
    print(x)
