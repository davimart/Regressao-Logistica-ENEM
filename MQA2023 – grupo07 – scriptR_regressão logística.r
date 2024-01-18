# Installing packages
if (!require(pROC)) install.packages("pROC")
library(pROC)
# Install and load the pscl package
if (!require(pscl)) install.packages("pscl")
library(pscl)

# For Logistic regression
if (!require(caTools)) install.packages("caTools")
library(caTools)

# For ROC curve to evaluate model
if (!require(ROCR)) install.packages("ROCR")
library(ROCR)

# Install and load the pROC package
if (!require(pROC)) install.packages("pROC")
library(pROC)

# Install and load the pscl package
if (!require(pscl)) install.packages("pscl")
library(pscl)

if (!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)

dataset <- 'MQA2023 – grupo07 – dataset_regressão logística.csv'
dados <- read.csv(dataset, sep=";")
summary(dados)

# Splitting dataset
split <- sample.split(dados, SplitRatio = 0.8)

train_reg <- subset(dados, split == "TRUE")
test_reg <- subset(dados, split == "FALSE")

# Training model

# X10Percentil_Geral
#Vinte_CincoPercentil_Geral
logistic_model <- glm(X10Percentil_Geral ~ Acesso_Internet + Sexo_Masculino +
                       Preta + Parda + Amarela + Indigena +
                       Pai_Ensino_Medio_Completo +
                       Pai_Ensino_Superior_Mais +
                       Mae_Ensino_Medio_Completo +
                       Mae_Ensino_Superior_Mais + Ate_1212 +
                       Entre_1212_e_3030 + Escola_SemResposta +
                       Escola_Publica,
                      data = train_reg,
                      family = "binomial")
summary(logistic_model)


#ODDSRATIO
# Assuming 'logistic_model' is your logistic regression model
coefficients <- coef(logistic_model)
conf_intervals <- confint(logistic_model)
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
conf_matrix <- table(Actual = test_reg$X10Percentil_Geral, Predicted = predicted_classes)

# Accuracy calculation
accuracy <- sum(diag(conf_matrix)) / sum(conf_matrix)
error_rate <- 1 - accuracy

# Print the confusion matrix and metrics
print("Confusion Matrix:")
print(conf_matrix)
print(paste("Accuracy:", round(accuracy, 3)))
print(paste("Error Rate:", round(error_rate, 3)))

pR2(logistic_model)

# Assuming 'logistic_model' is your logistic regression model
predicted_probabilities <- predict(logistic_model, newdata = test_reg, type = "response")

# Create a ROC curve and calculate AUC-ROC
roc_curve <- roc(test_reg$X10Percentil_Geral, predicted_probabilities)
auc_score <- auc(roc_curve)

# Print AUC-ROC
print(paste("AUC-ROC:", round(auc_score, 3)))