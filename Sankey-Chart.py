import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(node = dict(pad = 15,thickness = 20,

      line = dict(color = "black", width = 0.5),
      label = ["Y1_Base", "Y1_Silver", "Y1_Gold", "Y2_Base", "Y2_Silver", "Y2_Gold", "Y3_Base", "Y3_Silve", "Y3_Gold"],
      color = ['#a6cee3','#fdbf6f','#fb9a99','#a6cee3','#fdbf6f','#fb9a99',"pink","silver","gold" ]
    ),
    link = dict(
      source = [0, 0,0, 1, 1,1, 2 ,2, 5], # indices correspond to source node wrt to label 
      target = [3, 4, 5, 3, 4, 5, 5,3,0], 
      value = [18, 8, 2, 1, 16, 4 , 8, 1,1],
      color = ['#a6cee3', '#a6cee3', '#a6cee3', '#fdbf6f','#fdbf6f', '#fdbf6f', '#fb9a99', '#fb9a99','#fb9a99']
  ))])

fig.update_layout(
    hovermode = 'x',
    title="Sankey Chart",
    font=dict(size = 10, color = 'white'),
    plot_bgcolor='black',
    paper_bgcolor='white'
)

fig.show()
