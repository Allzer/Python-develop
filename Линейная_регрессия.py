{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMZLt5+W/Y4J3i+x5PnFZZ6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Allzer/Python-develop/blob/main/%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Работа с Pandas"
      ],
      "metadata": {
        "id": "AjYajqnFVTpd"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X1bqbCnr1ER8"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "from random import randint\n",
        "from sklearn.linear_model import LinearRegression"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "f = pd.read_csv('Lineregression.csv', encoding=\"latin-1\", sep=';')\n",
        "f"
      ],
      "metadata": {
        "id": "G3gLr3WBO7sL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f'название колонок: {f.columns}') #название колонок\n",
        "print(f'описание индексов: {f.index}') #описани индексов\n",
        "print(f'количество строк: {len(f)}') #количество строк\n",
        "print(f'количество строк и столбцов: {f.shape}') #количество строк и столбцов\n",
        "print(f'количество значений в таблице: {f.size}') #количество значений в таблице"
      ],
      "metadata": {
        "id": "WbubNbNKU7H0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "f['X'][:] #получаем столбец таблицы\n",
        "f[['X','Y']] #получаем больше одного столбца\n",
        "f.loc[0] #информация о строке в формате серии\n"
      ],
      "metadata": {
        "id": "xKFF-PYkRSd8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "f.rename(columns={'Èêñû ': 'X'}).rename(columns={'Èãðèêè':'Y'}) #переименование столбцов"
      ],
      "metadata": {
        "id": "CKkF8NEdT66k"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Делаем линейную регрессию"
      ],
      "metadata": {
        "id": "_tVfeuwnVOr2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "k = 2.8\n",
        "b = -3\n",
        "x = np.linspace(1,100, 100).reshape(-1,1).astype('int32')\n",
        "y = [i*k for i in range(100)]\n",
        "y = np.array(y).reshape(-1,1).astype('int32')\n"
      ],
      "metadata": {
        "id": "DUOh0MBPITMP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = LinearRegression().fit(x, y)\n",
        "y_p = model.predict(x)"
      ],
      "metadata": {
        "id": "-xwBgQK6-dtp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(x,y, s = 10)\n",
        "plt.plot(x,y_p, c ='r')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "1f-89Sf11MbD",
        "outputId": "af01490e-810d-42b3-8225-19a86823d592"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(model.coef_)\n",
        "print(model.intercept_)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rRXUxDnKcCeH",
        "outputId": "be51c9e5-7869-4884-f5f5-f3474d92c60d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[2.79914191]]\n",
            "[-3.18666667]\n"
          ]
        }
      ]
    }
  ]
}