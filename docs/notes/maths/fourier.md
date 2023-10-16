# Fourier

## Definitions

`Continuous signals`
: $\hat{f}(\omega) = \frac{1}{2\pi} \int f(t) e^{-i\omega t} dt$
: $f(t) = \int \hat{f}(\omega) e^{i\omega t} d\omega$

`Discrete signals`
: $X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-\frac {i 2\pi}{N}kn}$
: $x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k \cdot e^{\frac {i 2\pi}{N}kn}$

$\frac{1}{2\pi}$ and $\frac{1}{N}$ to ensure $\hat{F}(F(f)) = f$, depending on the convention used, can be on $f$,$\hat{f}$, or both

- position (radius) of the center of mass captures the strength of a frenquency
- angle (theta) of the center of mass captures the phase of a frequency

## Properties

| Property                  | Time Domain                                          | Frequency Domain                                      |
| ------------------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| Linearity                 | $a \cdot f(t) + b \cdot g(t)$                        | $a \cdot \hat{f}(\omega) + b \cdot \hat{g}(\omega)$   |
| Time Shifting             | $f(t - t_0)$                                         | $e^{-i\omega t_0} \cdot \hat{f}(\omega)$              |
| Frequency Shifting        | $e^{i\omega_0 t} \cdot f(t)$                         | $\hat{f}(\omega - \omega_0)$                          |
| Scaling                   | $f(at)$                                              | $\frac{1}{\|a\|} \cdot \hat{f}(\frac{\omega}{a})$     |
| Time Differentiation      | $\frac{df(t)}{dt}$                                   | $i\omega \cdot \hat{f}(\omega)$                       |
| Frequency Differentiation | $-itf(t)$                                            | $\frac{dF(\omega)}{d\omega}$                          |
| Time Convolution          | $f(t) \ast g(t)$                                     | $\hat{f}(\omega) \cdot \hat{g}(\omega)$               |
| Freq Convolution          | $f(t) \cdot g(t)$                                    | $\frac{1}{2\pi} \hat{f}(\omega) \ast \hat{g}(\omega)$ |
| Parseval's Theorem        | $\int \|f(t)\|^2 dt$                                 | $\int \| \hat{f}(\omega) \|^2 d\omega$                |
| Symmetry                  | $f(t)$ real $\Rightarrow$ $\hat{f}(\omega)$ even     | $f(t)$ even $\Rightarrow$ $\hat{f}(\omega)$ real      |
|                           | $f(t)$ imaginary $\Rightarrow$ $\hat{f}(\omega)$ odd | $f(t)$ odd $\Rightarrow$ $\hat{f}(\omega)$ imaginary  |

## Usual functions and transform

| Function                | Time Domain, $f(t)$                   | Frequency Domain, $\hat{f}(\omega)$                                     |
| ----------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| Impulse (Dirac Delta)   | $\delta(t)$                           | $1$                                                                     |
| Unit Step               | $u(t)$                                | $\frac{1}{i\omega} + \pi\delta(\omega)$                                 |
| Rectangular Pulse       | $\text{rect}\left(\frac{t}{T}\right)$ | $T \cdot \text{sinc}\left(\frac{\omega T}{2}\right)$                    |
| Gaussian                | $e^{-\pi t^2}$                        | $e^{-\pi\omega^2}$                                                      |
| Exponential             | $e^{at}$                              | $\frac{1}{a - i\omega}$                                                 |
| Sine Function           | $\sin(\omega_0t)$                     | $\pi\left[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)\right]$ |
| Cosine Function         | $\cos(\omega_0t)$                     | $\pi\left[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)\right]$ |
| Rectangular Function    | $\text{rect}\left(\frac{t}{T}\right)$ | $T\cdot \text{sinc}\left(\frac{\omega T}{2}\right)$                     |
| Triangular Function     | $\text{tri}\left(\frac{t}{T}\right)$  | $T^2 \cdot \text{sinc}^2\left(\frac{\omega T}{2}\right)$                |
| Delta Comb              | $\delta(t - nT)$                      | $2\pi\sum{\delta(\omega - 2\pi n/T)}$                                   |
| Heaviside Step Function | $H(t)$                                | $-\frac{i}{\omega} + \pi\delta(\omega)$                                 |
| Constant                | $A$                                   | $2\pi A\delta(\omega)$                                                  |

??? question "`Fourier transform` for continuous signals [](){.fbutton .ok}[](){.fbutton .nok}"
    : $\hat{f}(\omega) = \frac{1}{2\pi} \int f(t) e^{-i\omega t} dt$
    : $f(t) = \int \hat{f}(\omega) e^{i\omega t} d\omega$
    ##### id: 3bef8a, box: 2, score: 1/1, next: 17/10/2023, last: 16/10/2023

??? question "`Fourier transform` for discrete signal [](){.fbutton .ok}[](){.fbutton .nok}"
    : $X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-\frac {i 2\pi}{N}kn}$
    : $x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k \cdot e^{\frac {i 2\pi}{N}kn}$
    ##### id: fe298b, box: 1, score: 0/0, next: 06/10/2023, last: 06/10/2023

??? question "Fourier: Explain what $f(t)$ and $\omega$ represent [](){.fbutton .ok}[](){.fbutton .nok}"
    - position (radius) of the center of mass captures the strength of a frenquency
    - angle (theta) of the center of mass captures the phase of a frequency
    ##### id: 6ef80d, box: 3, score: 2/2, next: 17/10/2023, last: 11/10/2023

??? question "List 5 properties of fourier transform [](){.fbutton .ok}[](){.fbutton .nok}"
    | Property                  | Time Domain                                          | Frequency Domain                                      |
    | ------------------------- | ---------------------------------------------------- | ----------------------------------------------------- |
    | Linearity                 | $a \cdot f(t) + b \cdot g(t)$                        | $a \cdot \hat{f}(\omega) + b \cdot \hat{g}(\omega)$   |
    | Time Shifting             | $f(t - t_0)$                                         | $e^{-i\omega t_0} \cdot \hat{f}(\omega)$              |
    | Frequency Shifting        | $e^{i\omega_0 t} \cdot f(t)$                         | $\hat{f}(\omega - \omega_0)$                          |
    | Scaling                   | $f(at)$                                              | $\frac{1}{\|a\|} \cdot \hat{f}(\frac{\omega}{a})$     |
    | Time Differentiation      | $\frac{df(t)}{dt}$                                   | $i\omega \cdot \hat{f}(\omega)$                       |
    | Frequency Differentiation | $-itf(t)$                                            | $\frac{dF(\omega)}{d\omega}$                          |
    | Time Convolution          | $f(t) \ast g(t)$                                     | $\hat{f}(\omega) \cdot \hat{g}(\omega)$               |
    | Freq Convolution          | $f(t) \cdot g(t)$                                    | $\frac{1}{2\pi} \hat{f}(\omega) \ast \hat{g}(\omega)$ |
    | Parseval's Theorem        | $\int \|f(t)\|^2 dt$                                 | $\int \| \hat{f}(\omega) \|^2 d\omega$                |
    | Symmetry                  | $f(t)$ real $\Rightarrow$ $\hat{f}(\omega)$ even     | $f(t)$ even $\Rightarrow$ $\hat{f}(\omega)$ real      |
    |                           | $f(t)$ imaginary $\Rightarrow$ $\hat{f}(\omega)$ odd | $f(t)$ odd $\Rightarrow$ $\hat{f}(\omega)$ imaginary  |

    ##### id: 84d0c9, box: 2, score: 1/1, next: 12/10/2023, last: 11/10/2023

??? question "List 5 usual fourier transforms [](){.fbutton .ok}[](){.fbutton .nok}"
    | Function                | Time Domain, $f(t)$                   | Frequency Domain, $\hat{f}(\omega)$                                     |
    | ----------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
    | Impulse (Dirac Delta)   | $\delta(t)$                           | $1$                                                                     |
    | Unit Step               | $u(t)$                                | $\frac{1}{i\omega} + \pi\delta(\omega)$                                 |
    | Rectangular Pulse       | $\text{rect}\left(\frac{t}{T}\right)$ | $T \cdot \text{sinc}\left(\frac{\omega T}{2}\right)$                    |
    | Gaussian                | $e^{-\pi t^2}$                        | $e^{-\pi\omega^2}$                                                      |
    | Exponential             | $e^{at}$                              | $\frac{1}{a - i\omega}$                                                 |
    | Sine Function           | $\sin(\omega_0t)$                     | $\pi\left[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)\right]$ |
    | Cosine Function         | $\cos(\omega_0t)$                     | $\pi\left[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)\right]$ |
    | Rectangular Function    | $\text{rect}\left(\frac{t}{T}\right)$ | $T\cdot \text{sinc}\left(\frac{\omega T}{2}\right)$                     |
    | Triangular Function     | $\text{tri}\left(\frac{t}{T}\right)$  | $T^2 \cdot \text{sinc}^2\left(\frac{\omega T}{2}\right)$                |
    | Delta Comb              | $\delta(t - nT)$                      | $2\pi\sum{\delta(\omega - 2\pi n/T)}$                                   |
    | Heaviside Step Function | $H(t)$                                | $-\frac{i}{\omega} + \pi\delta(\omega)$                                 |
    | Constant                | $A$                                   | $2\pi A\delta(\omega)$                                                  |

    ##### id: afa94a, box: 2, score: 1/2, next: 14/10/2023, last: 13/10/2023
