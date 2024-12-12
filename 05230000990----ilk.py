is_martyr_veteran = "N"
consumer_amount_ind = 0
total_consumption_ind = 0
industrial_onvoice_big = 0
consumer_amount_pub = 0
total_consumption_pub = 0
public_single_consumption = 0
public_multi_consumption = 0
consumer_amount_res = 0
total_consumption_res = 0
consumer_amount_agr = 0
total_consumption_agr = 0
consumer_amount_lig = 0
total_consumption_lig = 0

multi_time_losers = 0
multi_time_users = 0

highest_resident_no = 0
highest_resident_amount = 0

highest_consumer_amount = 0



public_single_amount = 0
public_multi_amount = 0
profit_loss = 0

ELIGIBLE_CONSUMER_LIMIT = 1000

SINGLE_T_INDUSTRY = 3.051833
SINGLE_T_PUBLIC_LOW = 1.912220
SINGLE_T_PUBLIC_HIGH = 2.828414
SINGLE_T_RESIDENT_LOW = 0.482187
SINGLE_T_RESIDENT_HIGH = 1.132271
RESIDENT_VET = 0.061590
SINGLE_T_AGRICULT = 1.653096
LIGTHING = 2.595835

DAYT_INDUSTRY = 3.091833 
DAYT_PUBLIC = 2.858616
DAYT_RESIDENT = 1.157700
DAYT_AGRICULT = 1.704822

PEAKP_INDUSTRY = 4.909037
PEAKP_PUBLIC = 4.588843
PEAKP_RESIDENT = 2.083645
PEAKP_AGRICULT = 2.800325

NIGHTP_INDUSTRY = 1.625171
NIGHTP_PUBLIC = 1.481941
NIGHTP_RESIDENT = 0.417225
NIGHTP_AGRICULT = 0.771882

UNIT_DIST_INDUSTRY = 0.647998
UNIT_DIST_PUBLIC = 0.878175
UNIT_DIST_RESIDENT = 0.858883
UNIT_DIST_RESIDENT_VET = 0.582521
UNIT_DIST_AGRICULT = 0.721579
UNIT_DIST_LIGHTING = 0.841099

ECT_PERCENT_INDUSTRY = 0.01
ECT_PERCENT_NONINDUSTRY = 0.05

VAT_PERCENT_IND_PUB_LIGHT = 0.2
VAT_PERCENT_RES_AGRI = 0.1


def get_value(pre_meter_value, cur_meter_value, time): 
	pre_meter_value = int(input(f"Please enter your previous {time} period meter value: "))
	while pre_meter_value < 0:
		pre_meter_value = int(input("You have entered an invalid input. Please enter a valid input. "))
	cur_meter_value = int(input(f"Please enter your current {time} period meter value: "))
	while pre_meter_value > cur_meter_value:
		cur_meter_value = int(input("You have entered an invalid input. Please enter a valid input. "))
	return pre_meter_value, cur_meter_value


def get_consumption_amount(pre_meter_value, cur_meter_value):
	consumption_amount = cur_meter_value - pre_meter_value
	return consumption_amount


consumer_no = int(input("Please enter your consumer no: (Enter 0 to exit.) "))
while consumer_no != 0:
	consumer_type = input("Please enter your consumer type: (I/i/P/p/R/r/A/a/L/l) ")
	while consumer_type not in ['I','i','P', 'p', 'R', 'r', 'A', 'a', 'L', 'l']:
		consumer_type = input("You have entered an invalid input. Please enter a valid input. ")
	if consumer_type in ['r', 'R']:
		is_martyr_veteran = input("Are you the family of a martyr or veteran? (Y/y/N/n) ")
		while is_martyr_veteran not in ['Y', 'y', 'N', 'n']:
			is_martyr_veteran = input("You have entered an invalid input. Please enter a valid input. ")
	if consumer_type not in ['R', 'r'] and (is_martyr_veteran in ['Y', 'y'] ) or consumer_type not in ['l', 'L']:
		time_type = input("Are you using Single-time or Multi-time tariff: (S/s/M/m)")
		while time_type not in ["S", "s", "M", "m"]:
			time_type = input("You have entered an invalid input. Please enter a valid input. ")
	
	
	pre_dayt_per_meter, cur_dayt_per_meter = get_value(0, 0, "day time")
		
	pre_peak_per_meter, cur_peak_per_meter = get_value(0, 0, "peak period")
			
	pre_night_per_meter, cur_night_per_meter = get_value(0, 0, "night time")

			
	number_days = int(input("Please enter the number of days between previous and current reading: "))
	while number_days <= 0:
		number_days = int(input("You have entered an invalid input. Please enter a valid input. "))
		
	total_amount = int(input("Please enter your total electricity consumption in this year: "))
	while total_amount < 0:
		total_amount = int(input("You have entered an invalid input. Please enter a valid input. "))


	daytime_consumption = get_consumption_amount(pre_dayt_per_meter, cur_dayt_per_meter)

	peakperiod_consumption = get_consumption_amount(pre_peak_per_meter, cur_peak_per_meter)

	night_consumption = get_consumption_amount(pre_night_per_meter, cur_night_per_meter)

	total_consumption = daytime_consumption + peakperiod_consumption + night_consumption

	annual_consumption = total_consumption + total_amount


	if consumer_type in ['I', 'i']:
		if time_type in ['S', 's']:
			total_consumption_fee = total_consumption * SINGLE_T_INDUSTRY + total_consumption * SINGLE_T_INDUSTRY * ECT_PERCENT_INDUSTRY + total_consumption * UNIT_DIST_INDUSTRY
			total_consumption_ind += total_consumption
			industrial_consumption = total_consumption
		elif time_type in ['M', 'm']:
			total_consumption_fee = daytime_consumption * DAYT_INDUSTRY + peakperiod_consumption * PEAKP_INDUSTRY + night_consumption * NIGHTP_INDUSTRY + (DAYT_INDUSTRY + PEAKP_INDUSTRY + NIGHTP_INDUSTRY) * UNIT_DIST_INDUSTRY
			total_consumption_ind += total_consumption
			industrial_consumption = total_consumption
		ect_amount = total_consumption * SINGLE_T_INDUSTRY * ECT_PERCENT_INDUSTRY
		vat_amount = total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT
		invoice_amount = (total_consumption_fee) + (total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT)
		profit_loss = ((total_consumption * SINGLE_T_INDUSTRY + total_consumption * SINGLE_T_INDUSTRY * ECT_PERCENT_INDUSTRY + UNIT_DIST_INDUSTRY * total_consumption) + (total_consumption * SINGLE_T_INDUSTRY + total_consumption * SINGLE_T_INDUSTRY * ECT_PERCENT_INDUSTRY + UNIT_DIST_INDUSTRY * total_consumption) * VAT_PERCENT_IND_PUB_LIGHT) - (daytime_consumption * DAYT_INDUSTRY + peakperiod_consumption * PEAKP_INDUSTRY + night_consumption * NIGHTP_INDUSTRY + (DAYT_INDUSTRY + PEAKP_INDUSTRY + NIGHTP_INDUSTRY) * UNIT_DIST_INDUSTRY + UNIT_DIST_INDUSTRY * total_consumption) + (daytime_consumption * DAYT_INDUSTRY + peakperiod_consumption * PEAKP_INDUSTRY + night_consumption * NIGHTP_INDUSTRY + (DAYT_INDUSTRY + PEAKP_INDUSTRY + NIGHTP_INDUSTRY) * UNIT_DIST_INDUSTRY + UNIT_DIST_INDUSTRY * total_consumption) * VAT_PERCENT_IND_PUB_LIGHT
		consumer_amount_ind += 1 
		if highest_consumer_amount < invoice_amount:
			highest_consumer_amount = invoice_amount
			highest_consumer_no = consumer_no
			highest_consumer_type = 'Industry'
			highest_daily_consumption = industrial_consumption / number_days
		if invoice_amount > 100000 or industrial_consumption > 10000:
			industrial_onvoice_big += 1
	
	elif consumer_type in ['P', 'p']:
		if time_type in ['S', 's']:
			if total_consumption <= 30 * number_days:
				total_consumption_fee = total_consumption * SINGLE_T_PUBLIC_LOW + total_consumption * SINGLE_T_PUBLIC_LOW * ECT_PERCENT_INDUSTRY + total_consumption * UNIT_DIST_PUBLIC
				total_consumption_pub += total_consumption
				public_single_amount += 1
				public_single_consumption += total_consumption
			else:
				total_consumption_fee = total_consumption * SINGLE_T_PUBLIC_HIGH +  total_consumption * SINGLE_T_PUBLIC_HIGH * ECT_PERCENT_INDUSTRY + UNIT_DIST_PUBLIC
				total_consumption_pub += total_consumption
				public_single_amount += 1
				public_single_consumption += total_consumption
		if time_type in ['M', 'm']:
			total_consumption_fee = daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC + (daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC) * ECT_PERCENT_NONINDUSTRY +  (DAYT_PUBLIC + PEAKP_PUBLIC + NIGHTP_PUBLIC) * UNIT_DIST_PUBLIC
			total_consumption_pub += total_consumption
			public_multi_amount += 1
			public_multi_consumption += total_consumption
		ect_amount = (daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC) * ECT_PERCENT_NONINDUSTRY
		vat_amount = total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT
		invoice_amount = total_consumption_fee + vat_amount
		if total_consumption_fee <= 30 * number_days:
			profit_loss = ((total_consumption * SINGLE_T_PUBLIC_LOW + total_consumption * SINGLE_T_PUBLIC_LOW * ECT_PERCENT_INDUSTRY) +  total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT) - ((daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC + (daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC) * ECT_PERCENT_NONINDUSTRY +  (DAYT_PUBLIC + PEAKP_PUBLIC + NIGHTP_PUBLIC) * UNIT_DIST_PUBLIC) + (total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT))
		elif total_consumption_fee > 30 * number_days:
			profit_loss = ((total_consumption * SINGLE_T_PUBLIC_HIGH + total_consumption * SINGLE_T_PUBLIC_HIGH * ECT_PERCENT_INDUSTRY) +  total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT) - ((daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC + (daytime_consumption * DAYT_PUBLIC + peakperiod_consumption * PEAKP_PUBLIC + night_consumption * NIGHTP_PUBLIC) * ECT_PERCENT_NONINDUSTRY +  (DAYT_PUBLIC + PEAKP_PUBLIC + NIGHTP_PUBLIC) * UNIT_DIST_PUBLIC) + (total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT))
		consumer_amount_pub += 1
		if highest_consumer_amount < invoice_amount:
			highest_consumer_amount = invoice_amount
			highest_consumer_no = consumer_no
			highest_consumer_type = 'Public and Private Services Sector and Other'
			highest_daily_consumption = total_consumption / number_days
	
	
	elif consumer_type in ['R', 'r']:
		if is_martyr_veteran in ['Y', 'y']:
			total_consumption_fee = total_consumption * RESIDENT_VET + total_consumption * RESIDENT_VET * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_RESIDENT_VET
			total_consumption_res += total_consumption
			resident_consumption = total_consumption
		if is_martyr_veteran in ['N', 'n']:

			if time_type in ['S', 's']:
				if total_consumption <= 8 * number_days:
					total_consumption_fee = total_consumption * SINGLE_T_RESIDENT_LOW + total_consumption * SINGLE_T_RESIDENT_LOW * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_RESIDENT
					total_consumption_res += total_consumption
					resident_consumption = total_consumption

				else:
					total_consumption_fee = total_consumption * SINGLE_T_RESIDENT_HIGH + total_consumption * SINGLE_T_RESIDENT_HIGH * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_RESIDENT
					total_consumption_res += total_consumption
					resident_consumption = total_consumption
			if time_type in ['M', 'm']:
				total_consumption_fee = (daytime_consumption * DAYT_RESIDENT + peakperiod_consumption * PEAKP_RESIDENT + night_consumption * NIGHTP_RESIDENT) + (daytime_consumption * DAYT_RESIDENT + peakperiod_consumption * PEAKP_RESIDENT + night_consumption * NIGHTP_RESIDENT) * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_RESIDENT
				total_consumption_res += total_consumption
				resident_consumption = total_consumption
		ect_amount = (daytime_consumption * DAYT_RESIDENT + peakperiod_consumption * PEAKP_RESIDENT + night_consumption * NIGHTP_RESIDENT) * ECT_PERCENT_NONINDUSTRY
		vat_amount = total_consumption_fee * VAT_PERCENT_RES_AGRI
		invoice_amount = total_consumption_fee + vat_amount
		consumer_amount_res += 1
		if resident_consumption > highest_resident_amount:
			highest_resident_amount = resident_consumption
			highest_resident_no = consumer_no
			highest_resident_invoice = invoice_amount
	
	elif consumer_type in ['A', 'a']:
		if time_type in ['S', 's']:
			total_consumption_fee = total_consumption * SINGLE_T_AGRICULT + total_consumption * SINGLE_T_AGRICULT * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_AGRICULT
			total_consumption_agr += total_consumption
		elif time_type in ['M', 'm']:
			total_consumption_fee = (daytime_consumption * DAYT_AGRICULT) + (peakperiod_consumption * PEAKP_AGRICULT) + ((night_consumption * NIGHTP_AGRICULT) + (daytime_consumption * DAYT_AGRICULT) + (peakperiod_consumption * PEAKP_AGRICULT) + (night_consumption * NIGHTP_AGRICULT)) * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_AGRICULT
			total_consumption_agr += total_consumption
		ect_amount = total_consumption * SINGLE_T_AGRICULT * ECT_PERCENT_NONINDUSTRY
		vat_amount = total_consumption_fee * VAT_PERCENT_RES_AGRI
		invoice_amount = total_consumption_fee + vat_amount
		profit_loss = ((total_consumption * SINGLE_T_AGRICULT + total_consumption * SINGLE_T_AGRICULT * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_AGRICULT) + (total_consumption * SINGLE_T_AGRICULT + total_consumption * SINGLE_T_AGRICULT * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_AGRICULT) * VAT_PERCENT_RES_AGRI) - ((daytime_consumption * DAYT_AGRICULT) + (peakperiod_consumption * PEAKP_AGRICULT) + ((night_consumption * NIGHTP_AGRICULT) + (daytime_consumption * DAYT_AGRICULT) + (peakperiod_consumption * PEAKP_AGRICULT) + (night_consumption * NIGHTP_AGRICULT)) * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_AGRICULT) * (((daytime_consumption * DAYT_AGRICULT) + (peakperiod_consumption * PEAKP_AGRICULT) + ((night_consumption * NIGHTP_AGRICULT) + (daytime_consumption * DAYT_AGRICULT) + (peakperiod_consumption * PEAKP_AGRICULT) + (night_consumption * NIGHTP_AGRICULT)) * ECT_PERCENT_NONINDUSTRY + total_consumption * UNIT_DIST_AGRICULT) * VAT_PERCENT_RES_AGRI)
		consumer_amount_agr += 1
		if highest_consumer_amount < invoice_amount:
			highest_consumer_amount = invoice_amount
			highest_consumer_no = consumer_no
			highest_consumer_type = 'Agriculutural Activities'
			if time_type in ['S', 's']:
				highest_daily_consumption = total_consumption / number_days
			elif time_type in ['M', 'm']:
				highest_daily_consumption = total_consumption / number_days

	elif consumer_type in ['L', 'l']:
		ect_amount = total_consumption * LIGTHING * ECT_PERCENT_NONINDUSTRY
		total_consumption_fee = total_consumption * LIGTHING + ect_amount + total_consumption * UNIT_DIST_LIGHTING
		total_consumption_lig += total_consumption
		vat_amount = total_consumption_fee * VAT_PERCENT_IND_PUB_LIGHT
		invoice_amount = total_consumption_fee + vat_amount
		consumer_amount_lig += 1
		if highest_consumer_amount < invoice_amount:
			highest_consumer_amount = invoice_amount
			highest_consumer_no = consumer_no
			highest_consumer_type = 'Lighting'
			highest_daily_consumption = total_consumption / number_days

	
	print(f"Consumer no: {consumer_no}")
	
	if consumer_type in ['I', 'i']:
		print(f"Consumer type: Industry")
	elif consumer_type in ['P', 'p']:
		print(f"Consumer type: Public and Private Services Sector and Other")
	elif consumer_type in ['R', 'r']:
		print(f"Consymer type: Residental")
	elif consumer_type in ['A', 'a']:
		print(f"Consumer type: Agricultural Activities")
	elif consumer_type in ['L', 'l']:
		print(f"Consumer type: Lighting")

	print(f"Daytime period electricity consumption amount: {daytime_consumption} kWh")
	print(f"Peak period electricity consumption amount: {peakperiod_consumption} kWh")
	print(f"Night period electricity consumption amount: {night_consumption} kWh")
	print(f"Total electricity consumption amount: {total_consumption} kWh")
	print(f"Total electricity consumption fee: {total_consumption_fee:.2f} TL")
	print(f"ECT amount to be transferred to the municipality: {ect_amount:.2f} TL")
	print(f"VAT amount to be transferred to the state {vat_amount:.2f} TL")
	print(f"Total invoice amount: {invoice_amount:.2f} TL")

	if not (is_martyr_veteran in ['Y', 'y']) and (consumer_type in ['L', 'l']):
		if profit_loss > 0 and time_type in ['S', 's']:
			print(f"You would have lost {profit_loss:.2f} TL if you were using Multi-time tariff")
		elif profit_loss < 0 and time_type in ['S', 's']:
			print(f"You would have saved {profit_loss:.2f} TL if you were using Multi-time tariff")
		elif profit_loss > 0 and time_type in ['M', 'm']:
			print(f"you would have saved {profit_loss:.2f} TL if you were using Single-time tariff")
			multi_time_losers += 1
			multi_time_users += 1
		elif profit_loss < 0 and time_type in ['M', 'm']:
			print(f"You would have lost {profit_loss:.2f} TL if you were using Single-time tariff")
			multi_time_users += 1

	print(f"Your total electricity consumption in this year: {annual_consumption} kWh")
	if annual_consumption >= ELIGIBLE_CONSUMER_LIMIT:
		print("You deserve to be a free consumer.")
	else:
		print("You do not deserve to be a free consumer.")

	consumer_no = int(input("Please enter your consumer no: (Enter 0 to exit.) "))


total_consumer_amount = consumer_amount_agr + consumer_amount_ind + consumer_amount_lig + consumer_amount_pub + consumer_amount_res


print("STATISTICS: ")

print("| Industrial type consumer: ")
print(f" | Number of consumers: {consumer_amount_ind} ")
print(f" | Percentage of consumers: %{consumer_amount_ind/total_consumer_amount * 100}")
print(f" | Average electricity consumption amount: {total_consumption_ind/consumer_amount_ind} kWh")
print(f" | Total electricity consumption amount: {total_consumption_ind} kWh")

print("| Public and Private Services and Other type consumer: ")
print(f" | Number of consumers: {consumer_amount_pub} ")
print(f" | Percentage of consumers: %{consumer_amount_pub/total_consumer_amount * 100}")
print(f" | Average electricity consumption amount: {total_consumption_pub/consumer_amount_pub} kWh")
print(f" | Total electricity consumption amount: {total_consumption_pub} kWh")

print("| Residental type consumer: ")
print(f" | Number of consumers: {consumer_amount_res} ")
print(f" | Percentage of consumers: %{consumer_amount_res/total_consumer_amount * 100}")
print(f" | Average electricity consumption amount: {total_consumption_res/consumer_amount_res} kWh")
print(f" | Total electricity consumption amount: {total_consumption_res} kWh")

print("| Agricultural Activities type consumer: ")
print(f" | Number of consumers: {consumer_amount_agr} ")
print(f" | Percentage of consumers: %{consumer_amount_agr/total_consumer_amount * 100}")
print(f" | Average electricity consumption amount: {total_consumption_agr/consumer_amount_ind} kWh")
print(f" | Total electricity consumption amount: {total_consumption_agr} kWh")

print("| Lighting type consumer: ")
print(f" | Number of consumers: {consumer_amount_lig} ")
print(f" | Percentage of consumers: %{consumer_amount_lig/total_consumer_amount * 100}")
print(f" | Average electricity consumption amount: {total_consumption_lig/consumer_amount_ind} kWh")
print(f" | Total electricity consumption amount: {total_consumption_lig} kWh")

print(f"Bornova's total electricity coonsumption is {total_consumption_agr + total_consumption_pub + total_consumption_res + total_consumption_agr + total_consumption_lig} kWh.")

print(f"{public_single_amount} of Public and Private Services and Other consumers are using Single-time tariff. That is %{public_single_amount/(public_single_amount + public_multi_amount) * 100} of all Public and Private Services and Other consumers. Their average daily electric consumption is {public_single_consumption / number_days} kWh.")

print(f"{public_multi_amount} of Public and Private Services and Other consumers are using Multi-time tariff. That is %{public_multi_amount/(public_single_amount + public_multi_amount) * 100} of all Public and Private Services and Other consumers. Their average electric consumption is {public_multi_consumption / number_days} kWh.")

print(f"{industrial_onvoice_big} of Industry type consumers consumed 10000 kWh electricity or got 100000 TL onvoice. That is %{industrial_onvoice_big/consumer_amount_ind * 100} of all industry type consumers. ")

print(f"Consumer no: {highest_resident_no} has the highest consumption in this period. Consumer's daily average consumption is {highest_resident_amount / number_days} and total bill is {highest_resident_invoice}")

print(f"Consumer that has the highest total bill other than residental type consumers is the consumer with no: {highest_consumer_no} . Consumer's type is {highest_consumer_type}. daily average consumption amount is {highest_daily_consumption} kWh and total bill amount is {highest_consumer_amount:.2f} TL")

print(f"GDZ corporation's total revenue is {total_consumption_fee:.2f} TL ")
print(f"Municipality's total revenue is {ect_amount:.2f} TL ")
print(f"State's total revenue is {vat_amount:.2f} TL ")

print(f" %{multi_time_losers / multi_time_users * 100} of the consumers who choose Multi-time tariff made a loss.")