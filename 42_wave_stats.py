"""Distinct Python example #42."""
import wave,sys
with wave.open(sys.argv[1],"rb") as f:print({"channels":f.getnchannels(),"rate":f.getframerate(),"frames":f.getnframes(),"duration":f.getnframes()/f.getframerate()})
