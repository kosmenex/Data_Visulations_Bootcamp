""" Bu içerik global ai hub tarafından sunulan veri analizi bootcamp notlarındna oluşur
Eğitmen Ömer Cengiz hocanın slaytlarındaki bilgileri ve kodları kapsar."""
# Görselleştirme Tipleri
# Line Plot: çizgi grafiği, iki sayısal değer kümesi arasındaki ilişkiyi göstermek için kullanılır.genellikle iki bağımlı değişken arasında artan veya azalan bir eğilim göstermek için uygundur.
import sys
import matplotlib
from numpy import sin
from matplotlib import pyplot
x=[x*0.1 for x in range(100)]
y=sin(x)
pyplot.plot(x,y)
pyplot.show()

