import io
from flask import Response, Flask
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
plt.rcParams["figure.autolayout"] = True     #ustawia opcję automatycznego dostosowywania układu wykresu(aby skalować)
app = Flask(__name__)
@app.route('/a=<a>/b=<b>/c=<c>/xmin=<xmin>/xmax=<xmax>/ymin=<ymin>/ymax=<ymax>')       #pozwala na mapowanie adresu URL
def plot_png(a, b, c, xmin, xmax, ymin, ymax):                    #który jest kontenerem dla wykresu
   fig = Figure()
   axis = fig.add_subplot(1, 1, 1)                                #wykres paraboli 
   x = np.arange(float(xmin), float(xmax), 1)                     #tworzy tablicę x
   y = float(a) * x ** 2 + float(b) * x + float(c)                #oblicza wartości y
   axis.plot(x, y)
   plt.xlim([xmin, xmax])                                         #ustawiają zakres osi x
   plt.ylim([ymin, ymax])
   output = io.BytesIO()
   FigureCanvas(fig).print_png(output)
   return Response(output.getvalue(), mimetype='image/png')



