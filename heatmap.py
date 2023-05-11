""" Bu içerik global ai hub tarafından sunulan veri analizi bootcamp notlarındna oluşur
Eğitmen Ömer Cengiz hocanın slaytlarındaki bilgileri ve kodları kapsar."""
# Heatmap: Matrisin değerini görselleştirmek için renkleri kullanarak yapılan grafiktir.
# Yoğun ve fazla veriler koyu renkte, seyrek ve az olan veriler açık renkte temsil edilir.
# Korelasyon haritaları olarak bilinir ve karmaşıklık matrislerinde sıkça kullanılır
# Data Science için en önemli grafiktir.

import numpy as np
import seaborn as sns
np.random.seed(0)
uniform_data=np.random.rand(10,15)
ax=sns.heatmap(uniform_data)