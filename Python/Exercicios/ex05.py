{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Digite um número: 5\n",
      "Analisando o valor 5, seu antecessor é 4 e o sucessor é 6\n"
     ]
    }
   ],
   "source": [
    "n = int(input('Digite um número: '))\n",
    "a = n - 1\n",
    "s = n + 1\n",
    "print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))\n",
    "\n",
    "#Também da pra utilizar sem as variaveis utilizando so o format mas se o código for maior tera complicações.\n",
    "\n",
    "#Ex: n = int(input('Digite um número: '))\n",
    "#print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
