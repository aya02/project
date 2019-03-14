import numpy as np
from numpy import linalg

def call(n):

  A0 = np.random.rand(n,n)

  n = A0.shape[0]
  A_i = A0[:]
  Q_final = np.identity(n)

  for i in range(n-1):
  
    N = A_i.shape[0]
    x = A_i[:,0]
    alpha = np.linalg.norm(x)

    e = np.zeros(N)
    e[0] = 1
    u = x -alpha*e
    v = u/np.linalg.norm(u)

    Q_i = np.identity(N) -2*v*v.reshape(N,1)
    QQ = np.block([ [np.identity(i), np.zeros([i,N])], [np.zeros([N,i]), Q_i]])
    Q_final = np.dot( Q_final, QQ.T )

    QA = np.dot( Q_i, A_i )
    A_i = QA[1::,1::]


  R = np.dot( Q_final.T, A0 )

  print("A :")
  print(A0)
  print("Q :")
  print(Q_final)
  print("R :")
  print(R)

