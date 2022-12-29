import pytest
import time
import json
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class OrangeHRM_tester:
	def __init__(self):
		return

	def set_driver(self, brower):

		if brower == 'chrome':
			self.driver = webdriver.Chrome(ChromeDriverManager().install())
		elif brower == 'edge':
			self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
		elif brower == 'firefox':
			self.driver = webdriver.Firefox()
		else:
			raise Exception("Invalid browser")

	def PIM_page_test(self, browser ='chrome', csv_path = "PIM_test_data.csv"):
		df = pd.read_csv(csv_path)
		result = []
		include_list = ['Current Employees Only', 'Current and Past Employees',  'Past Employees Only']
		status_list = ['Freelance', 'Full-Time Contract', 'Full-Time Pernament', 'Full-Time Probation', 'Part-Time Contract', 'Part-Time Internship']
		title_list = ['Account Assistant', 'Chief Executive Officer', 'Chief Finacial Officer', 'Chief Technical Officer', 'Content Specialist', 
			'Customer Success Manager', 'Database Administrator', 'Finance Analyst', 'Finance Manager', 'Head of Support', 'HR Associate',
			'HR Manager', 'IT Manager', 'Network Administrator', 'Payroll Administrator', 'Pre-Sales Coordinator', 'QA Engineer', 'QA Lead',
			'Sales Representative', 'Social Media Marketer', 'Software Architect', 'Software Engineer', 'Support Specialist', 'VP - Client Services', 'VP - Sales & Marketing']
		sub_unit_list = ['OrangeHRM', 'Engineering', 'Development', 'TechOps', 'Quality Assurance', 'Sales & Marketing', 'Sales', 'Marketing', 'Client Services',
			'Technical Support', 'Finance', 'Human Resources', 'Business Analytics', 'Research', 'Production', 'Accounting', 'Operation Management', 'Information Technology', 'Purchase', 'Public Relation']
		for index, row in df.iterrows():
			try:
				self.set_driver(browser)
				self.login("Admin", "Admin@123")
				
				self.driver.find_element(By.LINK_TEXT, "PIM").click()

				WebDriverWait(self.driver, 10).until(
			    EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-left-space"))
			)


				# Set input
					# employee name
				print(row['Employments Status'])
				if not pd.isna(row['Employee Name']):
					self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").click()
					self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input").send_keys(row['Employee Name'])

					# supervisor name
				if not pd.isna(row['Supervisor Name']):
					self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[5]/div/div[2]/div/div/input").click()
					self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[5]/div/div[2]/div/div/input").send_keys(row['Supervisor Name'])

					# supervisor name
				if not pd.isna(row['Employee Id']):
					self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div[2]/input").click()
					self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div[2]/input").send_keys(row['Employee Id'])
				
				if not pd.isna(row['Employments Status']):
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[1]').click()
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[{}]'.format(status_list.index(row['Employments Status']) + 2)).click()

				if not pd.isna(row['Include']):
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').click()
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[{}]'.format(include_list.index(row['Include']) + 1)).click()
				
				if not pd.isna(row["Job Title"]):
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div').click()
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[{}]'.format(title_list.index(row['Job Title']) + 2)).click()

				if not pd.isna(row["Sub Unit"]):
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]').click()
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[{}]'.format(sub_unit_list.index(row['Sub Unit']) + 2)).click()

				#submit form
				self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-left-space").click()


				# assert output
				have_error_message = True
				try:
					WebDriverWait(self.driver, 5).until(
				    		EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-input-field-error-message")))
				except:
					try:
						WebDriverWait(self.driver, 5).until(
				    		EC.presence_of_element_located((By.XPATH, "//div[@id='oxd-toaster_1']/div")))
					except:
						have_error_message = False
				if row['Expected Result'] == 'Search success':
					assert not have_error_message
				else:
					assert have_error_message

				#end test
				self.logout()
				self.driver.quit()
				result.append("PASSED")
			except:
				self.driver.save_screenshot("{}_{}.png".format(browser, row['Description']))
				self.driver.quit()
				result.append("FAILED")


		#export report
		df['browser'] = browser
		df['result'] = result
		df.to_csv("TEST_RESULT_"+ browser+ "_" + csv_path)

	def leave_page_test(self, browser = 'chrome', csv_path = "Leave_test_data.csv"):
		sub_unit_list = ['OrangeHRM', 'Engineering', 'Development', 'TechOps', 'Quality Assurance', 'Sales & Marketing', 'Sales', 'Marketing', 'Client Services',
			'Technical Support', 'Finance', 'Human Resources', 'Business Analytics', 'Research', 'Production', 'Accounting', 'Operation Management', 'Information Technology', 'Purchase', 'Public Relation']
		#read csv file
		df = pd.read_csv(csv_path)
		result = []
		for index, row in df.iterrows():
			try:
				self.set_driver(browser)
				self.login("Admin", "Admin@123")

				#Go to leave page
				self.driver.find_element(By.LINK_TEXT, "Leave").click()
				WebDriverWait(self.driver, 10).until(
			    EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-button--secondary"))
			)
				#choosing data
					#from date
				element = self.driver.find_element(By.XPATH, "//div/div[2]/div/div/input")
				element.send_keys(Keys.CONTROL + "a")
				element.send_keys(Keys.DELETE)
				element.send_keys(row['From Date'])

					# to date
				element = self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/input")
				element.send_keys(Keys.CONTROL + "a")
				element.send_keys(Keys.DELETE)
				element.send_keys(row['To Date'])

					# Leave Type
				if pd.isna(row['Show Leave with Status']):
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/span/i').click()
				
				if not pd.isna(row["Sub Unit"]):
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]').click()
					self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[{}]'.format(sub_unit_list.index(row['Sub Unit']) + 2)).click()

					# name
				if not pd.isna(row['Employee Name']):
					self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").click()
					self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").send_keys(row['Employee Name'])

					# include past employee
				if row['Include Past Employees'] == True:
					self.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input").click()
				#submit form
				
				self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
				#assert result
				have_error_message = True
				try:
					WebDriverWait(self.driver, 5).until(
				    		EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-input-field-error-message")))
				except:
					try:
						WebDriverWait(self.driver, 5).until(
				    		EC.presence_of_element_located((By.XPATH, "//div[@id='oxd-toaster_1']/div")))
					except:
						have_error_message = False
				if row['Expected Result'] == 'Search success':
					assert not have_error_message
				else:
					assert have_error_message


				#end test
				self.logout()
				self.driver.quit()
				result.append("PASSED")

			except Exception as e:
				self.driver.save_screenshot("{}_{}.png".format(browser, row['Description']))
				self.driver.quit()
				result.append("FAILED")

		#export report
		df['browser'] = browser
		df['result'] = result
		df.to_csv("TEST_RESULT_" + browser+ "_" + csv_path)

	def test_with_many_browser(self, func):
		for key in ['chrome', 'firefox', 'edge']:
			func(browser = key)

	def login(self, username, password):
		#self.set_driver('chrome')
		self.driver.get("http://localhost:8181/web/index.php/auth/login")
		self.driver.set_window_size(1536, 864)

		#enter username
		username_input = WebDriverWait(self.driver, 10).until(
		    EC.presence_of_element_located((By.NAME, "username"))
		)
		
		username_input.click()
		username_input.send_keys(username)


		#enter password
		password_input = self.driver.find_element(By.NAME, "password")
		password_input.click()
		password_input.send_keys(password)

		#click login
		self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()

		#verify login
		username_input = WebDriverWait(self.driver, 10).until(
		    EC.presence_of_element_located((By.LINK_TEXT, "Dashboard"))
		)
		

	def logout(self):
		self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-tab").click()

		logout_option = WebDriverWait(self.driver, 10).until(
		    EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
		)
		logout_option.click()

		#verify logout
		WebDriverWait(self.driver, 10).until(
		    EC.presence_of_element_located((By.CLASS_NAME, "orangehrm-login-button"))
		)

tester = OrangeHRM_tester()

tester.test_with_many_browser(tester.PIM_page_test)
tester.test_with_many_browser(tester.leave_page_test)
