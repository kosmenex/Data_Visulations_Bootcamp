""" Bu içerik global ai hub tarafından sunulan veri analizi bootcamp notlarındna oluşur
Eğitmen Ömer Cengiz hocanın slaytlarındaki bilgileri ve kodları kapsar."""
# Histogram: Sayısal bir öğe listesi için veri dağılımını göstermek için kullanılır.7
# X eksenindeki gösterilen sürekli değişken, ayrık aralıklarla bölünür ve o ayrık aralıkta sahip oladuğunuz veri sayısı çubuğun yüksekliğini belirtir.
#  Histogram, değerlerin nerede yoğunlaştığını, uç noktaların neler olduğunu ve veri kümesinde herhangi bir boşluk olup olmadığı bilgisini verir
import seaborn as sns
penguins=sns.load_dataset("penguins")
penguins.head()
penguins.describe().T
sns.histplot(data=penguins, x="flipper_length_mm")