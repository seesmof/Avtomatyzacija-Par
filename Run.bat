TODO replace the path with appropriate one
if not exist "./data/packages_info.txt" (
  echo Installing requirements...
  pip install -r requirements.txt
  echo Requirements installed successfully ✝️💓 praise Jesus Christ our Holy Lord GOD Almighty > "./data/packages_info.txt"
)

TODO replace python script path with appropriate one
python ./src/main.py
exit