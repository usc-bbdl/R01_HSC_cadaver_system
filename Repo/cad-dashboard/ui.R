library(shiny)

# Define UI for miles per gallon application
shinyUI(fluidPage(  
  # Application title
  titlePanel("Data reviewer for Cadaver Experiments"),
  
  # Sidebar with controls to select the variable to plot against
  # mpg and to specify whether outliers should be included
  sidebarLayout(
    sidebarPanel(
      textInput("dataPath", label = h3("Path to data files"), 
                value = "c:/data"), 
      
      htmlOutput("timestampSelector") 
    ),

    mainPanel(
      tabsetPanel(
        type = "tabs",   
        tabPanel("FPGA",                  
                 plotOutput("fpgaPlot"), 
                 plotOutput("ddd")
                 ),        
        tabPanel("Loadcell", 
                 plotOutput("loadcellPlot"), 
                 plotOutput("aaa")
                 ),
        tabPanel("Encoder",                  
                 plotOutput("encoderPlot"), 
                 plotOutput("bbb")
                 ),
        tabPanel("Pertubot", 
                 plotOutput("pertubotPlot"),
                 plotOutput("ccc")
                 )

      )
    )
  )
))
