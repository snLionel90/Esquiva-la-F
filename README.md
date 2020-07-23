Copyright © Lionel Sanchez
Juego: Esquiva el Bloque F

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
------------------------------------------------------------------------------------------
descarge el repositorio con:
<ul><li>$ git clone https://github.com/snLionel90/Esquiva-la-F.git</li></ul> 

El repositorio contiene el script de configuracion setup.py, ejecutelo con:
<ul>
  <li>$ cd %nombre directorio descarga% </li>
  <li>$ python setup.py install</li>
 </ul>
 
 <h2>se requiere de extensiones de; pygame</h2>
<ul>
  <li>py -m pip install pygame</li> 
  <li>py -m pip install tkinter</li>
  
</ul>
---------------------------
<h1>Esquiva los proyectiles utilizando las teclas de flechas, indicado en el siguiente parrafo</h1>

<h3>Esta Condicion indica la accion de eventos del teclado para el movimiento del objeto en pantalla.:</h3>
<ul>
<li>for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            he_chocado =True
        # si se pulsa una tecla el vehiculo se mueve
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                incremento_x =-5        
            if evento.key == pygame.K_RIGHT:
                incremento_x =5              
            if evento.key == pygame.K_UP:
                incremento_y = -5
            if evento.key == pygame.K_DOWN:
                incremento_y = 5  
                </li>
</ul>

<ul>
<li>La Tecla flecha derecha, desplaza el vehiculo hacia la horizontal derecha.</li>
<li>La Tecla Flecha izqierda, desplaza el vehiculo hacia la horizontal izquierda</li>
<li>La Tecla Flecha Arriba, desplaza el vehiculo hacia la vertical superior o hacia arriba</li>
<li>La Tecla Flecha abajo, desplaza el vehiculo hacia la vertical inferior o hacia abajo</li>
<ul>

<h2> si no se pulsa ninguna tecla el vehiculo se detiene y podria colisionar con un misil</h2>


