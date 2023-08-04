#Pairs Trading

library(Quandl)
library(shiny)
library(plotly)
library(rsconnect)
library(dplyr)
library(egcm)
library(shinydashboard)
library(shinythemes)

end_date <- Sys.Date()
start_date <- Sys.Date() - 365

#Finacial Sector
mahindra_finance <- Quandl("NSE/MMFIN", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
mahindra_finance[c(2,3,4,5,7,8)] <- NULL
colnames(mahindra_finance)[c(2)] <- c("mahindra_finance_Close")

capital_first <- Quandl("NSE/CAPF",api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
capital_first[c(2,3,4,5,7,8)] <- NULL
colnames(capital_first)[c(2)] <- c("Capital_Close")

edelweiss <- Quandl("NSE/EDELWEISS", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
edelweiss[c(2,3,4,5,7,8)] <- NULL
colnames(edelweiss)[c(2)] <- c("Edelweiss_Close")

icici_prudential <- Quandl("NSE/ICICIPRULI", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
icici_prudential[c(2,3,4,5,7,8)] <- NULL
colnames(icici_prudential)[c(2)] <- c("ICICI_Close")

iifl_holdings <- Quandl("NSE/IIFL", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
iifl_holdings[c(2,3,4,5,7,8)] <- NULL
colnames(iifl_holdings)[c(2)] <- c("IIFL_Close")

motilal_oswal <- Quandl("NSE/MOTILALOFS", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
motilal_oswal[c(2,3,4,5,7,8)] <- NULL
colnames(motilal_oswal)[c(2)] <- c("Motilal_Close")

network_18 <- Quandl("NSE/NETWORK18", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
network_18[c(2,3,4,5,7,8)] <- NULL
colnames(network_18)[c(2)] <- c("Network_Close")

bharat_fin <- Quandl("NSE/BHARATFIN", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
bharat_fin[c(2,3,4,5,7,8)] <- NULL
colnames(bharat_fin)[c(2)] <- c("Bharat_Close")

pilani_invest <- Quandl("NSE/PILANIINVS", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
pilani_invest[c(2,3,4,5,7,8)] <- NULL
colnames(pilani_invest)[c(2)] <- c("Pilani_Close")

finance_choice <- c( "Bharat Fin", "Capital First", "Edelweiss", "ICICI Prudential", "IIFL Holdings", "Motilal Oswal", "Network 18", "Pilani Invest", "Mahindra Finance")

data_close <- cbind(bharat_fin,capital_first[c(-1)], edelweiss[c(-1)], icici_prudential[c(-1)], iifl_holdings[c(-1)],  motilal_oswal[c(-1)], network_18[c(-1)], pilani_invest[c(-1)], mahindra_finance[c(-1)])
#fix(data_close)

colnames(data_close)[c(2,3,4,5,6,7,8,9,10)] <- finance_choice

#Auto Industry.
mahindra_auto <- Quandl("NSE/MM", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
mahindra_auto[c(2,3,4,5,7,8)] <- NULL
colnames(mahindra_auto)[c(2)] <- c("Mahindra_Auto_Close")

atul_auto <- Quandl("NSE/ATULAUTO", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
atul_auto[c(2,3,4,5,7,8)] <- NULL
colnames(atul_auto)[c(2)] <- c("Atul_Auto_Close")

isuzu_auto <- Quandl("NSE/SMLISUZU", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
isuzu_auto[c(2,3,4,5,7,8)] <- NULL
colnames(isuzu_auto)[c(2)] <- c("Isuzu_Auto_Close")

tvs_auto <- Quandl("NSE/TVSMOTOR", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
tvs_auto[c(2,3,4,5,7,8)] <- NULL
colnames(tvs_auto)[c(2)] <- c("TVS_Auto_Close")

tata_auto <- Quandl("NSE/TATAMOTORS", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
tata_auto[c(2,3,4,5,7,8)] <- NULL
colnames(tata_auto)[c(2)] <- c("TATA_Auto_Close")

ashok_auto <- Quandl("NSE/ASHOKLEY", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
ashok_auto[c(2,3,4,5,7,8)] <- NULL
colnames(ashok_auto)[c(2)] <- c("Ashok_Auto_Close")

maruti_auto <- Quandl("NSE/MARUTI", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
maruti_auto[c(2,3,4,5,7,8)] <- NULL
colnames(maruti_auto)[c(2)] <- c("Maruti_Auto_Close")

auto_choice <- c("Mahindra&Mahindra", "Atul Auto", "SML Isuzu", "TVS Motors", "TATA Motors", "Ashok Leyland", "Maruti Suzuki")

data_close <- cbind(data_close, mahindra_auto[c(-1)],atul_auto[c(-1)],isuzu_auto[c(-1)], tvs_auto[c(-1)], tata_auto[c(-1)], ashok_auto[c(-1)],  maruti_auto[c(-1)])
#fix(data_close)

colnames(data_close)[c(11,12,13,14,15,16,17)] <- auto_choice

#Pharma Sector
piramal_pharma <- Quandl("NSE/PEL", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
piramal_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(piramal_pharma)[c(2)] <- c("Piramal_Pharma_Close")

lupin_pharma <- Quandl("NSE/LUPIN", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
lupin_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(lupin_pharma)[c(2)] <- c("Lupin_Pharma_Close")

cipla_pharma <- Quandl("NSE/CIPLA", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
cipla_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(cipla_pharma)[c(2)] <- c("Cipla_Pharma_Close")

drreddy_pharma <- Quandl("NSE/DRREDDY", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
drreddy_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(drreddy_pharma)[c(2)] <- c("Dr Reddy_Pharma_Close")

sun_pharma <- Quandl("NSE/SPARC", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
sun_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(sun_pharma)[c(2)] <- c("Sun Pharma_Close")

glenmark_pharma <- Quandl("NSE/GLENMARK", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
glenmark_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(glenmark_pharma)[c(2)] <- c("Glenmark_Pharma_Close")

biocon_pharma <- Quandl("NSE/BIOCON", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
biocon_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(biocon_pharma)[c(2)] <- c("Biocon_Pharma_Close")

glaxo_pharma <- Quandl("NSE/GLAXO", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
glaxo_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(glaxo_pharma)[c(2)] <- c("Glaxo_Pharma_Close")

auro_pharma <- Quandl("NSE/AUROPHARMA", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
auro_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(auro_pharma)[c(2)] <- c("Aurobindo_Pharma_Close")

pfizer_pharma <- Quandl("NSE/PFIZER", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
pfizer_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(pfizer_pharma)[c(2)] <- c("Pfizer_Pharma_Close")

abbott_pharma <- Quandl("NSE/ABBOTINDIA", api_key="yhDgzi5iqrT89Yzri3Uz", start_date = start_date, end_date = end_date, order = 'asc')
abbott_pharma[c(2,3,4,5,7,8)] <- NULL
colnames(abbott_pharma)[c(2)] <- c("Abbott_Pharma_Close")

pharma_choice <- c( "Piramal Pharma", "Lupin", "Cipla", "Dr Reddy", "Sun Pharma", "Glenmark", "Biocon","GlaxoSmithKline", "Aurobindo Pharm", "Pfizer", "Abbott India")

data_close <- cbind(data_close, piramal_pharma[c(-1)], lupin_pharma[c(-1)],cipla_pharma[c(-1)], drreddy_pharma[c(-1)], sun_pharma[c(-1)], glenmark_pharma[c(-1)], biocon_pharma[c(-1)], glaxo_pharma[c(-1)], auro_pharma[c(-1)], pfizer_pharma[c(-1)], abbott_pharma[c(-1)])
#fix(data_close)

colnames(data_close)[c(18,19,20,21,22,23,24,25,26,27,28)] <- pharma_choice


full_choice <- c("Finance Sector", "Auto Industry", "Pharmaceutical")

ui <- fluidPage(shinythemes::themeSelector(),
                titlePanel("Pairs Trading"),
                dashboardSidebar(width = 150,
                                 radioButtons(inputId = "fullchoice", label = strong("Select the Sector"), choices = full_choice, selected = "")
                ),
                conditionalPanel(
                  condition = "input.fullchoice == 'Finance Sector'",
                  sidebarPanel(width = 4,
                               selectInput(inputId = "first", label = strong("First Share"), choices = finance_choice, selected = ""),
                               selectInput(inputId = "second", label = strong("Second Share"), choices = finance_choice , selected = "")
                  ), mainPanel(
                    plotlyOutput(outputId = "time_series"),
                    verbatimTextOutput(outputId = "egcm")
                  )
                ),
                conditionalPanel(
                  condition = "input.fullchoice == 'Auto Industry'",
                  sidebarPanel(width = 4,
                               selectInput(inputId = "first1", label = strong("First Share"), choices = auto_choice, selected = ""),
                               selectInput(inputId = "second1", label = strong("Second Share"), choices = auto_choice , selected = "")
                  ),
                  mainPanel(
                    plotlyOutput(outputId = "time_series1"),
                    verbatimTextOutput(outputId = "egcm1")
                  )),
                conditionalPanel(
                  condition = "input.fullchoice == 'Pharmaceutical'",
                  sidebarPanel(width = 4,
                               selectInput(inputId = "first2", label = strong("First Share"), choices = pharma_choice, selected = ""),
                               selectInput(inputId = "second2", label = strong("Second Share"), choices = pharma_choice , selected = "")
                  ),
                  mainPanel(
                    plotlyOutput(outputId = "time_series2"),
                    verbatimTextOutput(outputId = "egcm2")
                  )
                ))



server <- function(input, output){
  output$time_series <- renderPlotly({plot_ly() %>% 
      add_lines(x = ~data_close$Date, y = ~log(data_close[,input$first]), mode = "lines") %>%
      add_lines(x = ~data_close$Date, y = ~log(data_close[,input$second]), mode = "lines") %>%
      layout(title = "Time-series", xaxis = list(title = "Time"), yaxis = list(title ="Movement"), showlegend =F) })
  output$egcm <- renderPrint(summary(egcm(data_close[,input$first], data_close[,input$second])))
  
  output$time_series1 <- renderPlotly({plot_ly() %>% 
      add_lines(x = ~data_close$Date, y = ~log(data_close[,input$first1]), mode = "lines") %>%
      add_lines(x = ~data_close$Date, y = ~log(data_close[,input$second1]), mode = "lines") %>%
      layout(title = "Time-series", xaxis = list(title = "Time"), yaxis = list(title ="Movement"), showlegend =F)}) 
  output$egcm1 <- renderPrint(summary(egcm(data_close[,input$first1], data_close[,input$second1])))
  
  output$time_series2 <- renderPlotly({plot_ly() %>% 
      add_lines(x = ~data_close$Date, y = ~log(data_close[,input$first2]), mode = "lines") %>%
      add_lines(x = ~data_close$Date, y = ~log(data_close[,input$second2]), mode = "lines") %>%
      layout(title = "Time-series", xaxis = list(title = "Time"), yaxis = list(title ="Movement"), showlegend =F)})
  output$egcm2 <- renderPrint(summary(egcm(data_close[,input$first2], data_close[,input$second2])))
}


shinyApp(ui = ui, server = server)
