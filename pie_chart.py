""" Bu içerik global ai hub tarafından sunulan veri analizi bootcamp notlarındna oluşur
Eğitmen Ömer Cengiz hocanın slaytlarındaki bilgileri ve kodları kapsar."""
# Pie Chart: Pasta grafiğidir. Kategorik değerlerin yüzde dağılımını gösterir.
# Bir bütünün parçaları arasındaki ilişki açıkça görülebilir
# grafiğin parçaları her kategorideki bütünün parçaları ile kesirli ortantılıdır.

import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
labels=["Apple","Banana","Cherry","Dates"]
plt.pie(y,labels=labels)
plt.show()