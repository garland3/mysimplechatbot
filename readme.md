![QABot](imgs/qabot.png)
![mobileQabot](imgs/qa2.png)




# Chat-bot test
* inspired by chatgpt
* can I do something similar? or perhaps just on a narrower task. 
* chatgpt seems to need 
- gpt
- training on code
- feedback on response in a RL with human feedback similar to an actor critic where you train a GPT model to be the critic . 

## Plan
* start with gpt2
* download some code
 - try github api (hit api limit)
 - try kaggle (ran out of space)
 * just get a model from huggingface (OK, this is what I'm using. )

 # Starting on chabotv2

 ```bash
 conda create --name chatbot python=3.10
 conda activate chatbot
 conda install pytorch torchvision torchaudio cudatoolkit=11.7 -c pytorch -c nvidia
 pip install transformers fastapi uvicorn ipython ipykernel dynaconf

```
# Status
* basic UI
* logging data to sqlite db
* uses huggingface model
* bot is dumb, needs to be trained