from display import Display
import threading
from eye import eye_func
thread = threading.Thread(target=eye_func)
thread.start()
x=Display()
x.run()
