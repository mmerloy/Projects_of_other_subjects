import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

print('Table')
data = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print(data)
print('Task#1')
print(data.groupby(["Sex"])["Survived"].value_counts(normalize=True))

print('Task#2')
describe_fields = ["Age", "Fare", "Pclass", "SibSp", "Parch"]
print("Статистика по числовым полям для мужчин: ")
male = data[data["Sex"] == "male"][describe_fields].describe()
print(male)
print('\n\n')
print("Статистика по числовым полям для женщин: ")
female = data[data["Sex"] == "female"][describe_fields].describe()
print(female)

print('Task#3')
print(data.groupby(["Embarked"])["Survived"].value_counts(normalize=True))

print('Task#4')
print(data["Name"].value_counts()[:10])

print('Task#5')
print(data.isnull().sum())
dict_value = {}
data["Embarked"] = data["Embarked"].fillna("Q")
data["Cabin"] = data["Cabin"].fillna("default")
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Fare"] = data["Fare"].fillna(data["Fare"].median())
print('Result')
print(data.isnull().sum())

print('Task#6')
print('Результат в новом new_test')


def new_data(data):
    data.loc[data["Embarked"] == "S", "Embarked"] = 9
    data.loc[data["Embarked"] == "C", "Embarked"] = 8
    data.loc[data["Embarked"] == "Q", "Embarked"] = 7
    data.loc[data["Sex"] == "male", "Sex"] = 9
    data.loc[data["Sex"] == "female", "Sex"] = 8
    return data


train_6 = new_data(data)
test_6 = new_data(test)
train_6 = train_6.dropna()
test_6 = test_6.dropna()

model = RandomForestClassifier(max_depth=11, n_estimators=100, max_features='sqrt')
model.fit(train_6[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]], train_6["Survived"])
predictions = model.predict(test_6[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]])
new_test_data = pd.DataFrame(
    {
    "PassengerId": test_6["PassengerId"],
    "Name": test_6["Name"],
    "Survived": predictions
    }
)
new_test_data.to_csv("new_test.csv", index=False)
