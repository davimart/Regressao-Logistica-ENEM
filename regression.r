# Lista de pacotes que você deseja instalar
install.packages("jsonlite")
pacotes <- c("pROC", "pscl", "caTools", "ROCR", "ggplot2", "fmsb")

# Instalação de pacotes ausentes
pacotes_instalar <- pacotes[!(pacotes %in% installed.packages()[,"Package"])]
if(length(pacotes_instalar) > 0) install.packages(pacotes_instalar)

# Carregamento de pacotes
pacotes_carregar <- pacotes[pacotes %in% installed.packages()[,"Package"]]
sapply(pacotes_carregar, require, character.only = TRUE)


dataset <- 'C:\\Users\\Davi Araujo\\Documents\\GitHub\\learning_projects\\Análise de Dados\\Regressão Logística\\MICRODADOS_ENEM_2022_PSICOLOGIA.csv'
dados <- read.csv(dataset, sep=";")
summary(dados)


# Splitting dataset
split <- sample.split(dados, SplitRatio = 0.8)

train_reg <- subset(dados, split == "TRUE")
test_reg <- subset(dados, split == "FALSE")

# Training model

# X10Percentil_Geral
#Vinte_CincoPercentil_Geral
logistic_model <- glm(Top_Geral ~ Sexo_Masculino +
  Preta + Parda + Amarela + Indigena + 
  Pai_Menos_que_Medio + Pai_Ensino_Medio_Completo + Pai_Ensino_Superior_Mais + 
  Mae_Menos_que_Medio + Mae_Ensino_Medio_Completo + Mae_Ensino_Superior_Mais +
  Pai_Grupo_1 + Pai_Grupo_2 + Pai_Grupo_3 +
  Pai_Grupo_4 + Pai_Grupo_5 + Mae_Grupo_1 +
  Mae_Grupo_2 + Mae_Grupo_3 + Mae_Grupo_4 + Mae_Grupo_5 + 
  Ate_1212 + Entre_1212_e_3030 + Escola_Publica + Escola_Privada + Acesso_Internet,
                      data = train_reg,
                      family = "binomial")

summary(logistic_model)

#ODDSRATIO
# Assuming 'logistic_model' is your logistic regression model
coefficients <- coef(logistic_model)
conf_intervals <- confint.default(logistic_model)
odds_ratios <- exp(coefficients)
odds_ratio_intervals <- exp(conf_intervals)

# Create a data frame
results_df <- data.frame(
  Predictor = names(coefficients),
  Coefficient = coefficients,
  Odds_Ratio = odds_ratios,
  Odds_Ratio_CI_Lower = odds_ratio_intervals[, 1],
  Odds_Ratio_CI_Upper = odds_ratio_intervals[, 2]
)

# Print the data frame
print(results_df)


# Predicting on the test set
predicted_probabilities <- predict(logistic_model, newdata = test_reg, type = "response")
predicted_classes <- ifelse(predicted_probabilities > 0.5, 1, 0)  # Assuming a threshold of 0.5

# Creating a confusion matrix
#X10Percentil_Geral
#Vinte_CincoPercentil_Geral
conf_matrix <- table(Actual = test_reg$Top_Geral, Predicted = predicted_classes)

# Accuracy calculation
accuracy <- sum(diag(conf_matrix)) / sum(conf_matrix)
error_rate <- 1 - accuracy

# Print the confusion matrix and metrics
print("Confusion Matrix:")
print(conf_matrix)
print(paste("Accuracy:", round(accuracy, 3)))
print(paste("Error Rate:", round(error_rate, 3)))


# Assuming 'logistic_model' is your logistic regression model
nagelkerke_r2 <- NagelkerkeR2(logistic_model)
print(nagelkerke_r2)
# Print the Nagelkerke's R^2 value
print(paste("Nagelkerke's R^2:", round(nagelkerke_r2, 3)))