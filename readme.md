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
 

 # Starting on chabotv2

 ```bash
 conda create --name chatbot python=3.10
 conda activate chatbot
 conda install pytorch torchvision torchaudio cudatoolkit=11.7 -c pytorch -c nvidia
 pip install transformers fastapi uvicorn ipython ipykernel

```
