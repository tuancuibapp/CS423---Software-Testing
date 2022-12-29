import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:8181/web/index.php/auth/login')

WebUI.setText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/input_Username_username'), 'admin1')

WebUI.setEncryptedText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/input_Password_password'), 'a627eoSpmGZbpVQxWE66kQ==')

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/button_Login'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/p_Admin 1'))

WebUI.verifyElementText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/p_Admin 1'), 'Admin 1')

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/a_Recruitment'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/li_Vacancies'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/button_Add'))

WebUI.setText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/input_Vacancy Name_oxd-input oxd-input--focus'), 
    vacancy_name)

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/i_-- Select --_oxd-icon bi-caret-up-fill ox_627fec'))

WebUI.setText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/textarea_Description_oxd-textarea oxd-texta_fed1e5'), 
    description)

WebUI.setText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/input'), 'Admin  1')

WebUI.setText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/input_Number of Positions_oxd-input oxd-inp_b37faf'), 
    number_of_positions)

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/button_Save'))

WebUI.rightClick(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/div_Edit VacancyVacancy NameJob TitleQA Eng_99b0dc'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/div_Edit VacancyVacancy NameJob TitleQA Eng_99b0dc'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/li_Vacancies'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/div_Vacan6'))

WebUI.verifyElementText(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/div_Vacan6'), vacancy_name)

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/i_Recruitment_oxd-icon bi-caret-down-fill o_253719'))

WebUI.click(findTestObject('Object Repository/recruitment_vacancy/Page_OrangeHRM/a_Logout'))

WebUI.closeBrowser()

