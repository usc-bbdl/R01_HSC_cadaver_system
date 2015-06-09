library(shiny)
library(datasets)

shinyServer(function(input, output) {
  
  # make dynamic selector
  output$timestampSelector <- renderUI({
    # Parse filenames for timestamp
    filenames<-rev(sort(list.files(path = input$dataPath)))
    fields <- sapply(filenames, function(x) c(strsplit(x, ".", fixed=TRUE)))
    getTimeStamp <- function(line) Reduce(function(x, y) paste(x, y, sep="."), line[1:4])
    timeStamps <- sapply(fields, getTimeStamp)
    
    # Dynamically generate the selector
    selectInput(inputId = "trial",
                label = "Choose Trial with Timestamp",
                choices = timeStamps,
                selected = 1)  
  })

  # Load and display the loadcell data
  loadcellInput <- reactive({
    read.csv(paste(input$dataPath, "/", input$trial, ".dev_loadcells.txt", sep=""))
  })
  output$loadcellPlot <- renderPlot ({
    par(mfrow=c(7,1))
    plot(loadcellInput()$time, loadcellInput()$ch1, type="l", col="blue")
    plot(loadcellInput()$time, loadcellInput()$ch2, type="l", col="blue")
    plot(loadcellInput()$time, loadcellInput()$ch3, type="l", col="blue")
    plot(loadcellInput()$time, loadcellInput()$ch4, type="l", col="blue")
    plot(loadcellInput()$time, loadcellInput()$ch5, type="l", col="blue")
    plot(loadcellInput()$time, loadcellInput()$ch6, type="l", col="blue")
    plot(loadcellInput()$time, loadcellInput()$ch7, type="l", col="blue")
  }, height = 1300)
  
  # Load and display the encoder data
  encoderInput <- reactive({
    read.csv(paste(input$dataPath, "/", input$trial, ".dev_encoders.txt", sep=""))
  })
  output$encoderPlot <- renderPlot ({
    par(mfrow=c(7,1))
    plot(encoderInput()$time, encoderInput()$ch1, type="l", col="blue")
    plot(encoderInput()$time, encoderInput()$ch2, type="l", col="blue")
    plot(encoderInput()$time, encoderInput()$ch3, type="l", col="blue")
    plot(encoderInput()$time, encoderInput()$ch4, type="l", col="blue")
    plot(encoderInput()$time, encoderInput()$ch5, type="l", col="blue")
    plot(encoderInput()$time, encoderInput()$ch6, type="l", col="blue")
    plot(encoderInput()$time, encoderInput()$ch7, type="l", col="blue")
  }, height = 1300)
  
#   # Load and display the pertubot (now Phantom) data
#   pertubotInput <- reactive({
#     read.csv(paste(input$dataPath, "/", input$trial, ".dev_phantom.txt", sep=""))
#   })
#   output$pertubotPlot <- renderPlot ({
#     par(mfrow=c(6,1))
#     plot(pertubotInput()$time, pertubotInput()$angx, type="l", col="blue")
#     plot(pertubotInput()$time, pertubotInput()$angy, type="l", col="blue")
#     plot(pertubotInput()$time, pertubotInput()$angz, type="l", col="blue")
#     plot(pertubotInput()$time, pertubotInput()$torx, type="l", col="blue")
#     plot(pertubotInput()$time, pertubotInput()$tory, type="l", col="blue")
#     plot(pertubotInput()$time, pertubotInput()$torz, type="l", col="blue")
#   }, height = 1300)   
  
  # Load and display the pertubot (now Phantom) data
  pertubotInput <- reactive({
    read.csv(paste(input$dataPath, "/", input$trial, ".dev_kinematic.txt", sep=""))
  })
  output$pertubotPlot <- renderPlot ({
    par(mfrow=c(6,1))
    plot(pertubotInput()$time, pertubotInput()$pos, type="l", col="blue")
    plot(pertubotInput()$time, pertubotInput()$pos, type="l", col="blue")
    plot(pertubotInput()$time, pertubotInput()$pos, type="l", col="blue")
    plot(pertubotInput()$time, pertubotInput()$pos, type="l", col="blue")
    plot(pertubotInput()$time, pertubotInput()$pos, type="l", col="blue")
    plot(pertubotInput()$time, pertubotInput()$pos, type="l", col="blue")
  }, height = 1300)   
  
  # FPGA data
  fpgaInput <- reactive({
    read.csv(paste("http://192.168.0.1/data/", input$trial, ".dev_fpga.txt", sep=""))
  })
  output$fpgaPlot <- renderPlot ({
    par(mfrow=c(6,1))
    plot(fpgaInput()$time, fpgaInput()$emg0, type="l", col="blue")
    plot(fpgaInput()$time, fpgaInput()$emg1, type="l", col="blue")
    plot(fpgaInput()$time, fpgaInput()$spinIa0, type="l", col="blue")
    plot(fpgaInput()$time, fpgaInput()$spinIa1, type="l", col="blue")
    plot(fpgaInput()$time, fpgaInput()$musLce0, type="l", col="blue")
    plot(fpgaInput()$time, fpgaInput()$musLce1, type="l", col="blue")
  }, height = 1300) 
  
})
