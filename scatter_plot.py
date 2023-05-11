""" Bu içerik global ai hub tarafından sunulan veri analizi bootcamp notlarındna oluşur
Eğitmen Ömer Cengiz hocanın slaytlarındaki bilgileri ve kodları kapsar."""
# Scatter Plot: Dağılım grafiğidir. Esas olarak iki sayısal grup arasındaki ilişkiyi dağınık noktalar çizmek için kullanılır.
# grafikteki her bir nokta tek bir gözlemdir.
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
x = 20 + randn(1000) + 100
y = x + (10 * randn(1000) + 50)

pyplot.scatter(x,y)
pyplot.show()
