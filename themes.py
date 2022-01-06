# import PySimpleGUI
import PySimpleGUI as sg
  
  
# Choose a Theme for the Layout
sg.theme('DarkTeal9')
  
layout = [[sg.Text('List of available themes')],
          [sg.Text('Please choose a theme to see the demo window')],
          [sg.Listbox(values = sg.theme_list(),
                      size =(20, 12),
                      key ='-LIST-',
                      enable_events = True)],
          [sg.Button('Exit')]]
  
window = sg.Window('Theme List', layout)

while True:  
    event, values = window.read()
      
    if event in (None, 'Exit'):
        break
          
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
      
# Close
window.close()