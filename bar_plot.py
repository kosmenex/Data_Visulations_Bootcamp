""" Bu içerik global ai hub tarafından sunulan veri analizi bootcamp notlarındna oluşur
Eğitmen Ömer Cengiz hocanın slaytlarındaki bilgileri ve kodları kapsar."""
# Bar Plot: Çubuk Grafiktir. Toplam, ortalama, medyan vb. işleviyle gruplanmış kategorik sütünlardan oluşur.
# farklı kategorideki verileri karşılaştırmak için kullanılır
# histogramla karıştırılmaması gerekir.
import seaborn as sns
tips=sns.load_dataset("tips")
tips.head()
tips.describe().T
sns.barplot(x="day",y="total_bill",data=tips)
