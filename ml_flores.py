from sklearn.datasets import load_iris # tabela de flores
import pandas as pd # manipulacao da tabela
from sklearn.model_selection import train_test_split  # fazer teste
from sklearn.neighbors import KNeighborsClassifier  # puxar o modelo knn
from sklearn.metrics import accuracy_score  # para ter uma previsao dos acertos
from sklearn.metrics import confusion_matrix
import seaborn as sns
import  matplotlib.pyplot as plt  # criar grafico

# carregar o datasets
iris= load_iris()

# transformando um dataframe para melhor vizualizar

data= pd.DataFrame(data=iris.data,columns=iris.feature_names)
data['target']= iris.target  # adicionar a coluna de especies


#adicionando uma coluna por especies
species_map = {0:'Iris-setosa',1:'Iris-versicolor',2:'Iris-verginica'}
data['species']=data['target'].map(species_map)

# mostrar as primeiras linhas

print(data.head())


x= iris.data   # caracteristicas de (inputs)
y = iris.target # os rotulos (classes)

# dividir em treino  (treino 70%) e teste  (teste 30%)

x_train,x_test,y_train,y_test,=train_test_split(x,y,test_size=0.3,random_state=42)


# criar o modelo knn com 3 vizinhos (classes)
knn =KNeighborsClassifier(n_neighbors=3)

#treinar o modelo com os dados de treino

knn.fit(x_train,y_train)

# fazer previsoes nos dados de teste

y_pred = knn.predict(x_test)

# agora avaliar a acuracia do modelo criado

acuracia = accuracy_score(y_test,y_pred)

print(f"acuracia de modelo knn: {acuracia*100:.2f}%")


# criando a matriz de confuçao
cm = confusion_matrix(y_test,y_pred)

# vizualizar a matriz

sns.heatmap(cm,annot=True,cmap='Blues',fmt='g')

plt.xlabel('previsao')
plt.ylabel('verdadeiro')
plt.show()



