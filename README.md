<h1 align="center">
  <br>
  <a><img src="https://i.ibb.co/V9FNKCy/Fram2e-1.png alt="ImagePixelizer "></a>
  <br>
  GeneratedPersonsParser
  <br>
</h1>
<p align="center">Parser of images of people generated by a neural network from <a href="https://generated.photos/">generated.photos</a> using their API</p>

## Features
 - You can use all filters of people's appearance
 - Can download an unlimited number of images per approach (it may only limit your API key)
 - Configuration file for options
 
 
## Compatibility
Check your Python version by typing in
```shell script
python --version
```
If you get the following
```shell script
Python 3.7.*
```
this script has been tested and confirmed to be supported.


## Usage
1. Go to the project folder and type in the console
```shell script
pip install -r requirements.txt
```
2. Then open *config.py* file and write path to images and output path.
settings = {
    "OUTPUT_PATH" : "YOUR_OUTPUT_PATH_HERE",
    "API_KEY" : "YOUR_API_KEY_HERE"
}

```
3 You can customize people filter editting persons_filter in *config.py*
```
# for example
persons_filter = {
    "AGE" : pd.Age.YOUNG,
    "SEX" : pd.Sex.MALE,
    "ETHNICITY" : pd.Ethnicity.ASIAN,
    "FACE" : pd.Face.UNDEFINED,
    "EMOUTION" : pd.Emoution.JOY,
    "HAIR" : pd.Hair.BLACK
}
```
Then just execute *launcher.py* script.

## Attention!
- Don't forget the slashes at the end of the pathes
- Use ```/``` or ```\\``` (on windows) in the pathes (not ```\``` )