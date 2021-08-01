class rental_prop():
    def __init__(self):
        self.prop_cost        = 200000
        self.prop_tax         = .007
        self.mortgage_period  = 30
        self.interest_rate    = .025
        self.rental_price     = 2000
        self.management_cost  = {
                                    "HOA": 135,
                                    "utilities": 20,
                                    "insurance": 135,
                                    "Maintenance":100
                                }    
        self.function_storage ={}
        self.other_income     = 0
        self.down_pay         = 50000
    def house_info (self):
        try:
            self.prop_cost=float(input('How much does your property cost?'))
            self.rental_price=float(input('How much do you rent your property to your tennants?'))
            self.prop_tax= float(input('What is the annual propety tax in your area? Put a whole number %'))/100.0
            self.mortgage_period= float(input('How many years is your mortgage period?'))
            self.interest_rate= float(input('How much is your mortgage interest rate? Enter a whole number %'))/100.0
            self.management_cost['HOA']=float(input('How much monthly HOA fees do you pay? If none, enter 0.'))
            self.management_cost['utilities']=float(input('How much monthly do you pay for utilities? If none, enter 0.'))
            self.management_cost['insurance']=float(input('How much do you pay for home owner insurance monthly?'))
            self.management_cost['Maintenance']=float(input('How much do you pay for monthly property maintenance? (Lawn keeping, pool service, etc'))
            self.down_pay= float(input('How much was your down payment? '))
        except:
            print('Enter a number please.')

    #monthly mortgage is house cost/monthly paymen of loan period with interest rate applied every month
    def mortgage_payment(self):
        monthly_mortgage=self.prop_cost/(self.mortgage_period*12)*(1+self.interest_rate)
        self.function_storage['monthly_mortgage']=round(monthly_mortgage,2)
        return monthly_mortgage
        

    #Monthly cashflow= net income-net expenses
    def monthly_cashflow (self):
        alt_source=input("Do you have another form of income from property? (laundry, parking, etc) yes/no ")
        try:
            alt_income=int(input("How much monthly income does this source bring in? Enter 0 if none "))
            self.other_income=alt_income
        except:
            print('You did not enter a number')
        mort=int(self.function_storage['monthly_mortgage'])
        hoa=self.management_cost['HOA']
        util=self.management_cost['utilities']
        ins=self.management_cost['insurance']
        maint=self.management_cost['Maintenance']
        alt=self.other_income
        tax=(self.prop_cost*self.prop_tax)/12
        #Cash flow calc
        cashflow= self.rental_price-mort-hoa-util-ins-maint-tax+alt
        self.function_storage['cashflow']= round(cashflow,2) 
        return cashflow
    #Cash on Cash Return on investment
    def roi (self):
        cash_on_cash = self.function_storage['cashflow']/self.down_pay
        return cash_on_cash

house= rental_prop()
house.house_info()
x=input('To calculate your ROI and cash Flow we need some basic we will need to know your mortgage payment. Ok/No ')
if x.lower()=='ok':
    mortgage = house.mortgage_payment()
    print(f'Your monthly mortgage payment will be:{round(mortgage,2)}')
    print('We will now calcualte your monthly cash flow')
    cash=house.monthly_cashflow()
    print(f'Your monthly cash flow is: ${round(cash,2)}')
    invest=house.roi()
    print(f'Your cash on cash return on investment will be: {round(invest,2)} %')
else:
    print('Have a good day!')
