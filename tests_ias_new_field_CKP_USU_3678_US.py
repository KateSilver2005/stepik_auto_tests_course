import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCkpFields:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.ok_fields = 0  # Инициализация счетчика совпадений
        self.wrong_field = 0  # Инициализация счетчика несовпадений
        yield  # Передать управление тесту
        self.browser.quit()  # Закрыть браузер после выполнения теста

    @pytest.mark.parametrize("uid", [
        'e155bb28-c503-c4d2-093e-b5fce68c3743',	'7a430339-c10c-642c-4b22-51756fd1b484',	'ac689931-e0da-618b-cf89-29a58b3124b8',
        'bdd88179-90ef-209f-0fb6-b049f2d2ea0c',	'b8842791-7fce-4b44-fa7e-0512d9d0ab9a',	'2808facb-4ea3-b7c9-fbfe-e09982783458',
        '53f43dac-ca35-184b-c37a-660c16988da8',	'1bf1cb46-b751-f9e7-3d86-fb51ef6eaad7',	'3ce6d3c8-830d-27ec-2e6a-1936ecbaa514',
        'eb8b3f50-0d12-feab-ec90-994f03f12225',	'da505d68-35f7-3789-38cf-98d67042effa',	'8e489b49-66fe-8f70-3b5b-e647f1cbae63',
        'e7aaccb8-5305-9f67-9dcc-b5fde01e1bcd',	'9f194f26-59e9-c228-019d-33543d03bf6e',	'd77e6859-6c15-c53c-2a33-ad143739902d',
        '2b278bd9-d0e5-9b02-2fca-723ea9b6d0c8',	'b28db90d-ca6f-49ad-ab33-196c9288a802',	'9023effe-3c16-b047-7df9-b93e26d57e2c',
        '52edc4a5-890a-dc59-cec8-2cb60f8af691',	'67880768-4201-4c83-ceda-dbe6b0ba0314',	'66b38b6e-25d2-be6f-041b-f83c5b1877cf',
        '3d5c70bb-4203-cdc2-d32d-538296c96bf5',	'f0dfac77-80a4-4232-30c0-985e5523cc5b',	'6e82873a-32b9-5af1-15de-1c414a1849cb',
        '494ba9ff-03bd-ad88-1378-a6fd4092a6c7',	'ce0a737d-f967-39eb-ece7-e9c07160e2ff',	'a4351b79-d9ea-3d84-2efa-89fae5d02b24',
        '9f8684e6-30c4-c30c-ad7b-1f0935cd62ab',	'cad40866-3854-c2c8-32d0-104dca5c7953',	'1d38372b-4726-3240-eb0d-0213fb020638',
        '3c74bf2b-6973-2660-34af-ab117ecf7de6',	'073b00ab-9948-7b74-b63c-9a6d2b962ddc',	'cc965788-4708-170e-160c-8372d92f3535',
        'b499bdfb-090a-be73-6c56-a9bc47d3cc2c',	'0e9d935f-7e3f-2b50-2450-c049ddbc7c92',	'2e0aca89-1f2a-8aed-f265-edf533a6d9a8',
        '0d8a39d0-e1c8-0662-93c2-877f928a326d',	'7486cef2-522e-e035-47cf-b970a404a874',	'b848edae-2587-6384-476f-8970b8491160',
        'a37685d3-8086-0ea8-7b3a-25290decf334',	'65d73258-3229-f7ae-a12a-962962e551c6',	'b6e71087-0acb-098e-5842-77457ba89d68',
        '036950f5-3144-2259-6c8f-808ae629431f',	'1ceebd48-4f8c-e6ee-116b-b50f71e59e49',	'91d679f8-9760-d1df-bcc1-1e8cb421177c',
        '667307e0-b82e-c60c-065d-17b35c5e412b',	'b887d8d5-e65a-c4de-c393-4028fe23ad72',	'3bf9acbd-9913-b775-15fd-7aef0e105a77',
        'e85c94e0-10b2-8b0a-2c50-34df6f1c4428',	'79514e88-8b8f-2aca-cc68-738d0cbb803e',	'faf40292-bba8-effc-1718-c732ee649677',
        '6174163d-4031-dae7-d004-fe4e87b87326',	'8cd19f01-74d2-03d3-485f-31d80fb49a8d',	'c5015c38-de6c-b1d4-6630-2f0f807ec85a',
        'df5a6bdf-0df4-9c21-a2ec-7afde7130298',	'399d75ad-f74b-8e16-14af-6772bf8d0045',	'84d34752-4ce3-3d88-ae1e-52092430bd4a',
        '15c8f2ff-bbc0-f143-001b-1edb6b0759b5',	'31fabf5f-469d-cb83-4191-a33262ba0026',	'0f28ba21-2f18-1c52-5228-bffbb2c27dba',
        'bb36f7d1-0644-7d47-ff7e-bb2c37c01f9d',	'a9528aeb-d6fe-34f6-c11a-5b04d9428619',	'1caa6360-0d14-3696-f9f4-3fb7019e69e1',
        'fedf67d6-f3d7-341c-1c1e-8a54774987d3',	'9e6a921f-bc42-8b56-38b3-986e365d4f21',	'7df5523b-b26e-62f3-2b12-cf0cebe3297d',
        '645e6bfd-d05d-1a69-c5e4-7b20f0a91d46',	'61347b85-4e50-08c1-e2e7-fdf5a613a1c0',	'b2184b42-f673-0c72-f9b7-7da247933997',
        '825e027d-2a22-ed4e-87de-e17b06606298',	'a2186aa7-c086-b46a-d4e8-bf81e2a3a19b',	'ccd2e3ea-a5c9-91ac-8809-91328c8f1463',
        '38ed162a-0dbe-f7b3-fe0f-628aa08b90e7',	'da9c986e-27ec-c4e4-3471-7a0ce957df80',	'2503fe18-f4e7-12eb-78f8-13f01e7b6840',
        'b30515d4-217c-30ee-b3c0-d29008bce6b2',	'4b21cf96-d4cf-612f-239a-6c322b10c8fe',	'cb073542-5b69-2126-f61b-83ab6a5bf9d0',
        '62f91ce9-b820-a491-ee78-c108636db089',	'4826928b-dd20-6614-d755-f7c1e4b1f711',	'7221e5c8-ec6b-08ef-6d3f-9ff3ce6eb1d1',
        '8caf4502-34fb-330f-df4e-677c9bd508ab',	'da520ebf-2888-a3ab-f61d-6baf697a8395',	'9e41eb32-24b2-35f6-dd5a-73652679e6b1',
        '0efd2c71-6308-0ddf-4a13-08e4325fe495',	'90ca8353-a563-4f5e-7188-43548febfa0a',	'5ba52225-c516-d9b7-f5d1-8293065efcae',
        '758cb892-692b-6874-629a-5dd14ad4fc7f',	'3a6102de-38d7-8a18-9af8-e9b8f0531826',	'4fa177df-2286-4518-b2d7-818d4db5db2d',
        'cd41a16f-a5c9-4e51-bff6-f879a025be0d',	'2c1449f1-bd3c-8b0b-93e8-89fbe2d1f2dc',	'45b5debc-22e9-2ef6-fe0c-4c8d4aaf97d5',
        '47833142-2bf8-91b4-eeb3-31114468750a',	'3222dd54-0009-81ff-ffa7-6b8ab21e0abd',	'33fa41eb-7df8-ca4a-96e7-6af006956313',
        '9b3fea2a-9012-aad6-88e1-d136f77ada0d',	'55d99a37-b2e1-badb-a7c8-df4ccd506a88',	'edfcbef7-932f-9be9-02ee-31bca35e2c1b',
        '563ca5e0-68bc-78b8-0791-0338bb4d4279',	'16fc18d7-8729-4ad5-1711-00e33d05d4e2',	'dba132f6-ab6a-3e3d-17a8-d59e82105f4c',
        '334fd9f7-7ee2-498a-6d36-583b1bed4fee',	'fbe3d186-3b97-4d6d-492a-c3c1ea44c779',	'f06828d3-538a-408a-c039-f1dd9efe9cb1',
        '35644abd-f343-3b07-c512-6f8fd0703bc7',	'17238786-2059-a126-d177-2b8bb418ed12',	'455c721c-826a-8015-7758-85e7ec551cdf',
        'ef4ddbbb-7c82-ef7b-5f16-2876bb9db400',	'36745e1f-5c74-b253-e1a7-d9c182dc2f4e',	'dff8e9c2-ac33-3815-46d9-6deea9922999',
        'cfcce062-1b49-c983-991e-ad4c3d4d3b6b',	'a2d10d35-5cde-bc87-9e4f-c6ecc6f63dd7',	'd4a89791-9a12-4958-e699-170b2b1dc8f2',
        'a81aeb28-312e-8276-862c-c498f478430d',	'9a96a2c7-3c0d-477f-f2a6-da3bf538f4f4',	'64025859-7cbc-5003-7072-712f964cf5d8',
        '344cfb56-dccb-f378-b1a5-f55e73efbe55',	'06eb4924-19eb-dc8a-d0ce-c7ec9f7bf8c8',	'731ae30a-f875-0c2d-2872-0ea3c1f8c2b1',
        'ef72d539-90bc-4805-684c-9b61fa64a102',	'96aae1bb-4c6c-705d-4741-3d146954750e',	'4aec1b34-35c5-2abb-df83-34ea0e7141e0',
        '936824c0-1919-5364-7ec6-09b4f49bc964',	'1c670a75-eea1-0572-8f9a-ab85b88b10da',	'51bfa4ca-2864-44e2-afaa-4127baff39c8',
        '133b3752-e52b-ae42-2303-64cb720f81f7',	'bdb6920a-dcd0-457a-a17b-53b22963dad9',	'e9a69336-b866-2306-67ef-2adc000329ac',
        '6fec24ea-c8f1-8ed7-93f5-eaad3dd7977c',	'c1d0f19c-3f82-7daf-0edd-3e69c3b195a9',	'937409a2-d5a4-0a13-c55b-e07d93d49757',
        '98f91497-5e74-23b8-742c-7655dcdb75a9',	'c9efe5f2-6cd1-7ba6-216b-be2a7d26d490',	'744a036b-6af8-1e01-4f36-8527e1db360a',
        'c50a969d-ba34-3afc-42ac-d8df71b0851a',	'be83b7ad-42a2-c053-c80a-64f952d8c5c0',	'522c5ecd-d183-c499-298b-931c32d5a41f',
        '06de0d1e-5799-4fba-28e2-7ace701d833f',	'804d5979-ca34-6294-ec6c-8712c6a051ff',	'cc3d69ed-781b-16bc-e066-87822ae56e6d',
        '93b2e3ec-ba9a-847b-2a79-824bea96fae5',	'ce60ff16-3cab-9702-9cc7-27e20e0fc3a7',	'f5c150af-bfbc-ef94-1def-203e85cf40bc',
        'ad8e88c0-f76f-a4fc-8e54-74384142a00a',	'766e428d-1e23-2bbd-d586-64b41346196c',	'432446d3-39de-d5b5-440e-848bfc57eabe',
        '72b38622-4056-bf94-0cd5-b01341f65e9d',	'54fda78a-a8a0-9b4d-77b5-aaec57b75028',	'42cd63cb-189c-30ed-03e4-2ce2c069566c',
        '75fc62fb-6044-5f9d-5cb3-729a9c62030a',	'bce8aa9d-e408-15b6-8ee8-88fbea41026e',	'8c9a14ff-ebb7-677d-033f-fce847991293',
        '97a53e6f-ca1e-bbc7-8999-5c5b70e98ced',	'6c0032cc-1f81-f6e5-5721-72f7910bebd4',	'0c86c250-a681-8631-a392-bbdad967d5a7',
        '07f1de39-7293-d02e-a1ee-1a1be4434dd5',	'ca1d3153-a1cf-0ed9-98d4-879fbb50d9ab',	'3cf98320-62e5-d81e-a58f-da7f5bbcbadf',
        '211ed78f-e919-38b9-0f84-a51944b08d5a',	'42c51d1b-e36f-0e8f-9777-29217afac1c0',	'b2adf274-eb5f-3707-dd26-8e4f1f679d23',
        '521b52df-480a-eb6b-cbae-5121b05d2771',	'399577b3-cc92-bbb7-d147-afbee73db577',	'7752239a-3992-c780-fe89-79e58a1067cd',
        '2b7b82a7-ec6d-e407-81fd-6ef338b41892',	'16b6fbe4-84ef-79a2-ee05-fb323ae61685',	'fee189e1-2b7f-0006-664f-b925b24e9f00',
        '35a3bd92-3d82-8e06-a353-c9993f8f3d7f',	'3540507b-5cbf-985c-bad0-bb61d0e39b58',	'29156891-8b9f-ffc0-13e9-24bc517f3591',
        'ffbd6cbb-019a-1413-183c-8d08f2929307',	'b44256af-3224-9c15-12f1-7330dd5e54bc',	'ab1e3dce-5f96-8863-b402-11501d75e42c',
        '202960b5-ba7b-d816-dc8e-974263208b2f',	'0cacb916-4f80-5455-edc9-2d1c37bd1d4d',	'a2f132c0-bc83-e043-8399-abef26a7ad0b',
        'e7a05e88-bc66-d80f-f670-29ad677347ba',	'bd54b6bc-6cc8-041d-e6ce-d1bfd21ce16d',	'8b76cc6a-5ff9-46b4-5cac-def580159401',
        'c1502ae5-a4d5-14ba-ec12-9f72948c266e',	'c91e3483-cf4f-9005-7d02-aa492d2b25b1',	'b22b257a-d051-9d45-0053-9da3c8bcf4dd',
        'b23f5220-2479-e957-b9ba-da847c1175d7',	'8d30aa96-e724-4075-9f74-bd2306c1fa3d',	'25766f01-628f-3d34-b93a-36a2301dffc9',
        'd6e01a82-fef1-9f84-8e8a-9a0aa238fc30',	'03604012-70d4-3703-cd7d-6295dba28ca9',	'e9f03bd8-de0d-3b98-26c1-be2cbe0d544e',
        '031ddc59-00aa-502b-7344-037391fa7650',	'0232cdfa-210d-e162-4507-44b3faf455c1',	'f5496252-609c-43eb-8a3d-147ab9b9c006',
        '065affbc-170e-2511-eeac-b3bd0e975ec1',	'2836be05-e71a-8f34-902a-6e6b37350134',	'68fda703-82b2-e225-72bd-f2f53224adca',
        '3b759cf7-e5a7-69c8-bd75-fd3d27a60b75',	'954497e6-895c-69b0-d1e4-c5581b01ee17',	'09060616-068d-2b95-44dc-33f2fbe4ce2d',
        'd73edcdf-8d40-28a6-c7b5-76d0188d433e',	'52b738b3-03d9-0a88-4137-546353e09ebb',	'154d6d1e-cf7c-9d3e-eefc-7f866eb0e80d',
        '0e5742ed-4edc-611e-061a-9b9dba46e2f7',	'34ec3164-18dc-57cf-8922-4ac0ff28f2ef',	'908c9a56-4a86-4265-85b2-9f5335b619bc',
        'e99190d1-185d-26e3-01f5-aa92f61a3853',	'5b63e9b6-3f4f-7a80-7485-fe3fa1cf2674',	'ecda6f9d-d545-35a9-7ef1-f3c6d710b8a7',
        '232d85e6-e892-51f9-0f2a-9cc4322660c8',	'47023ef0-a8aa-8af3-9688-6017bd682caf',	'52e75e99-fdc5-a9f9-c536-49c5812de29d',
        'b299ad86-2b6f-12cb-5767-9f0538eca514',	'29ac918d-a0cd-9566-d2bf-b7594dc5ab4f',	'62da8c91-ce7b-1084-6231-921795d6059e',
        '8ce5d989-374d-216a-867c-dc8871484b43',	'28d8b71a-76ad-7cc6-7168-6147a49790dc',	'0ebf1972-05c0-0fc6-e0aa-c7261a8c1bdc',
        '3a066efb-8cb5-340e-4ae3-7094a33216a1',	'6a05c7ea-4436-9a0c-75f5-2a6165ba4c71',	'ca3ec598-002d-2e76-62e2-ef4bdd58278b',
        '588d846d-aa28-720d-d279-70e3677d3278',	'f6b789be-22df-3f4e-327b-9c101272acee',	'8a50bae2-9780-7da9-e977-22a0b3fd8f27',
        'a60062a1-76c7-3df1-1b1d-f95971b84a8f',	'102a76c7-59e2-0e5c-1e3c-3930a162ccbd',	'9679c197-df2e-287d-9649-1476ccfedfdc',
        'c5d92566-89c4-3036-581f-781c61f26e50',	'2c9aff04-a09b-155f-a167-de590850976d',	'04ca0327-428e-f426-296a-ca487a49cd2a',
        '024421e3-1f2f-1e7a-f4c2-40ed36cc8507',	'f23841a4-23c6-5997-28f4-45768c0c642d',	'678beedb-fc69-1ec4-b9bb-b712f76a6b65',
        '4ad5a95f-fd13-7c0a-3aed-8ba1b40173f3',	'146000d7-bd39-1e0f-5f04-350553f963d4',	'c8f79c9d-9397-38fa-b8a5-d2f2da76c1d0',
        '799de6d3-dae4-c924-142c-f245a1d7f703',	'106f6c83-c83d-f067-118d-f6cb94526750',	'7371364b-3d72-ac9a-3ed8-638e6f0be2c9',
        '040a99f2-3e89-6076-3e68-0041c601acab',	'853fc462-0787-bcf1-e612-d79a463f670d',	'3f7bcd0b-3ea8-2268-3bba-8fc530f151bd',
        '00ee071f-7169-f8c2-b83b-80f19e3b4f97',	'14687ea7-319b-a650-3023-2cf73018fe02',	'6913fbfa-e9d8-f7a3-d555-2e1dd7662c54',
        '79b3a1e2-2709-1ad7-ef85-6b7dc62c813a',	'e3575ce0-b9a4-cfd8-3335-8ab37bc100df',	'c4d4d1fd-8feb-f93b-fa0b-e9ce91cab05b',
        '69c09730-4668-a17f-0afa-3d566c77b11c',	'd8ab1a52-f058-358b-947c-df8261b5e1a2',	'89d1d485-7b7c-85b4-aeda-baa36ac177ce',
        'b878a218-75f4-074d-8d69-29977d7b9795',	'20c86a62-8232-a67e-7bd4-6f76fba7ce12',	'e3aa0119-571f-7dc5-e1ff-b1b76faaea66',
        '8898e70d-4e27-c30a-d4a8-217660e7e16e',	'8503b221-040e-056d-a2bc-c23258f2da74',	'e8258e51-4031-7ff3-6c7f-8225a3bf9590',
        'f0b1d587-9866-f2c2-eba7-7f39993d1184',	'0a5c79b1-eaf1-5445-da25-2ada718857e9',	'60cc48ca-5112-7f6f-2a1a-f728696ee290',
        '4cf69b58-a8d9-7bac-2395-28f1c91d5a15',	'bc4c729a-408a-5310-1791-0aa252803778',	'59dfa2df-42d9-e3d4-1f5b-02bfc32229dd',
        '6cea1242-b0a6-0eab-1377-b6c3955f07d8',	'85ae750a-d1db-dc5c-2703-bcfe97e77152',	'0df5fc61-a96f-43d5-55f8-7011e848f6cd',
        '747d3443-e319-a227-47fb-b873e8b2f9f2',	'3b5020bb-8911-19b9-f513-0f1fea9bd773',	'2227d753-dc18-5050-3186-9d44673728e2',
        '10e818db-cef2-2e8e-6759-444e82a6756e',	'6869f62e-64a7-103d-0d95-7623a6d33d36',	'57d37bcb-54ea-4bd6-2b66-f4776c9f9f56',
        '3c959f1d-825f-57ce-0daf-93abe5b22144',	'6c4bb406-b3e7-cd54-47f7-a76fd7008806',	'9b63bee4-e20e-952e-8896-2eeced65081f',
        '30a3c4ad-4396-ab86-97fb-2d1ebf1d9fb3',	'0623461c-c436-6a3a-419f-fd74c9b13b8b',	'bb7c724d-adee-4b23-a595-f42c8f694240',
        'cfe5e55c-4964-7937-4176-83de9e93e71f',	'e8bf0f27-d70d-480d-3ab7-93bb7619aaa5',	'f0eaf559-f89c-a170-2278-3964ebe9cdfd',
        'a0ba2648-acd2-3dc7-a582-9968ce531a7d',	'd39608e5-8e7b-0b0d-26d9-e1d5c9da0e47',	'a9986cb0-6681-2f44-0bc2-bb6e3c13696c',
        '41f66692-1cc7-51e7-8e1f-27fcd9b9f735',	'94b5bde6-de88-8ddf-9cde-6748ad2523d1',	'd3157f2f-0212-a80a-5d04-2c127522a2d5',
        '206be63b-a052-3667-f0d3-58f2eb98d17a',	'd081c66c-5697-18f8-8c7e-9bfb9873fd31',	'e2eacaff-4678-7bfe-efca-a24cf35264c7',
        '91cf9ffa-a770-79e8-fc6c-183209bed17b',	'9cb9ed4f-35cf-7c2f-295c-c2bc6f732a84',	'd3967040-af69-ba48-b70f-89fd723940a8',
        '032dd17b-77fa-b7d5-1a47-6c5ff2b5659c',	'32b3ee02-7295-4b95-6a7d-1f86f76afa21',	'f18275c1-d73a-ad7e-c2cc-cacad5f65051',
        '2ef3e50f-d7c1-091d-da16-5f25be7f64fd',	'7a98af17-e63a-0ac0-9ce2-e96d03992fbc',	'5201acbd-0457-0672-2b3d-670125d183ef',
        '91378b33-1327-b40e-5643-90c43cd6b2be',	'2f3d0589-7cc6-2038-1763-eac5889f1807',	'ddac41d2-6311-5bd5-a68d-93389bb2df50',
        'fecaf344-2dc6-e4b1-e393-68fbee8dde48',	'99db67e1-91c6-9be7-91b5-c452e4c21e25',	'f4334c13-1c78-1e2a-6f0a-5e34814c8147',
        'f93c62ec-ee00-197f-c270-f318229a9c04',	'd0dfa378-a605-2f7d-8459-b53b22973a92',	'191db806-7950-9fce-6072-5e7543e793e2',
        'b0169350-cd35-566c-47ba-83c6ec1d6f82',	'82fd84c5-0c6c-63b7-286b-7857627a2966',	'292d90bc-c86f-e4a2-92a0-44ee2b769111',
        '405e8292-9b23-c05b-7711-05763b32f04c',	'aac61539-fd1f-b209-b44b-9f9d0d8d28ac',	'5bdd63f6-bdea-ec5d-33d5-beccbceca971',
        '6bd317c7-e4bd-9f80-1389-bd8878d7d6f8',	'512fc3c5-227f-637e-4143-7c999a2d3169',	'1aa494fd-1777-16de-4be2-a9810bb1edbb',
        '4a107ffb-fdfc-e06b-65e9-e80b06c56917',	'c1b70d96-5ca5-04aa-751d-db62ad69c63f',	'f0031c7a-91d7-4015-a9ad-dfbc589f3fe5',
        '79789a9b-92ac-e6f1-2275-ca09d7a77e0c',	'b9c3c00f-b907-e96e-0ce8-380ce80cfbde',	'bbfe382f-bc56-efc8-5371-d73cd2aa10ab',
        '8cf64126-053f-1379-6452-d3ab3bd83764',	'fb4eb365-8166-16b7-fbce-311de5b1cbbc',	'5086bb62-efba-a904-7fd1-4903c5959e9b',
        'c683b3aa-113f-5abc-9001-7f65a8187c42',	'8f775023-c755-f9f4-e3f7-abafabf40909',	'3f5ee243-547d-ee91-fbd0-53c1c4a845aa',
        '77ee3bc5-8ce5-60b8-6c2b-59363281e914',	'f402f3e7-f4bd-aa72-11f9-e3ea203cf3a5',	'03c8e789-d7bf-390c-1036-f6b31d59b3e8',
        '045a28d4-5db1-2cbf-c6f3-f992d7ee6c52',	'f925e8ee-22ad-aa93-72c7-22657c6dcac9',	'c828ef0b-f635-c240-ae57-103ffdd082c4',
        'f21306b9-ba4a-d09f-9aa8-1feb648b2686',	'f2f02055-2414-30ca-fb59-4eb34155a87c',	'dcbac0a1-19d7-cdf6-507e-e772da8c04cc',
        '60ad8380-1910-ec97-6590-f69f638e0d6d',	'08449cba-ce22-bc3d-8c62-2e83d21dcc38',	'3eb414bf-1c2a-66a0-9c18-5d60553417b8',
        '41ceae7e-c214-01a2-c8b2-c96ab6f9afcc',	'24c5433e-bd46-2cde-4657-e041c4f17f45',	'8fb8e4fd-c4f7-9d41-04c8-ac8d2e0fa4f9',
        '7a4bf9ba-2bd7-7406-8ad5-0351fb898076',	'dd61b41d-5b91-a9a0-9e50-4f025a87553b',	'a7ee126f-4b1c-d3b3-41cc-51e1950bd321',
        '37e7897f-62e8-d91b-1ce6-0515829ca282',	'db3a7840-8f46-e797-a88d-ef66a9b3fbd7',	'155b31c5-bc72-b8aa-1063-f9d1a643ab39',
        '4b600867-90c7-a6d2-72e2-c16aedff8ab0',	'43626ead-f550-e4a2-8616-fba3f4a43392',	'6a4d5952-d4c0-18a1-c1af-9fa590a10dda',
        '140a0da3-6875-f16b-6282-6f24ceb2ee37',	'2c995b67-5da1-3b75-2f00-b39f815f3328',	'4f13d33f-1ec7-b4c1-28e2-a3aa40b7c6f9',
        'c57abe86-de4e-516e-12df-a386053fbfe2',	'01ecf373-c53f-bda3-2d1e-8b51c9d876e4',	'58a00370-aa4d-d933-a07f-7e9f399fb52f',
        '7edfd522-20e2-032e-7281-061c82401195',	'1e377ca7-e646-e02a-1be5-8d2594c6b6d0',	'a34e7140-e696-f433-d7ca-3db620fb01b5',
        'ff4991ec-69d2-8375-d576-7d476e94c10c',	'177540c7-bcb8-db31-697b-601642eac8d4',	'f916a75e-055a-6b4d-c104-90b0186e2ac7',
        'be80f28e-9015-dc59-3f00-dd5d3b0c806d',	'1ce127c2-ee84-65ea-3338-bdb30fdafa21',	'57d33078-16e0-858e-e279-575e12634571',
        '8fa85083-ec87-3a43-4d58-d2b75f55ca07',	'36ed197b-3f31-618f-dbad-b3df86f804bd',	'cc431fd7-ec44-37de-061c-2577a4603995',
        '3485e5a4-8c5e-855f-0991-65468297f06d',	'20534044-25ba-e199-a81d-c64193f17471',	'03bfc1d4-7839-66c6-9cc6-aef8247e0103',
        '305d610a-a42d-55e8-6560-7bc60b971bba',	'472e7508-aca9-1462-9928-5ad27aa4a3b2',	'c6bc4401-1881-b526-ad20-9bbdb63f0f09',
        'e971093d-8253-95db-b8ec-570a26449b7a',	'cdba39dc-0f88-0550-f378-47b0a323e87b',	'8d15091c-ce98-3070-1423-e356154f1169',
        '4ea83d95-1990-d8bf-07a6-8ec3e50f9156',	'd3384f84-518d-5b75-144b-bf93e49e144b',	'ba95d78a-7c94-2571-1853-08775a97a3a0',
        '3742d9e4-9bf9-2f79-ad9f-8d4cd3517c3f',	'638add4b-ab71-ce43-541c-22d91658f643',	'629c169a-e782-1f11-e5da-586a4b738f70',
        'c5e79cce-d112-e354-10f5-6fe8f27210d7',	'09c4313d-a482-f2f8-1a8f-8340ed35392d',	'4517efac-5c9b-61ce-0795-91dfe4cffc7c',
        '4a140eaf-eab0-8951-9081-129709ced3df',	'65a31da7-ede4-dc9b-03fb-5bbf8f442ce9',	'a92c274b-8be4-96fb-05d9-5033552eeddd',
        '8b313cbf-3099-9888-de32-da1ec83ff503',	'7f01c939-7615-97f9-b832-694d4c381512',	'51cfed28-811d-67ae-c2e7-1efb6e10be02',
        '36a1ec62-f2a3-4665-8619-fee304e888ec',	'df839716-73de-5c8e-71ca-1e2645718dad',	'16f50624-c809-cd55-a150-3ba9b4841ea3',
        'b98249b3-8337-c508-8bbc-660d8f872d6a',	'74ac2ee9-8f7e-ea44-0383-c9616d2e3c23',	'fa84632d-742f-2729-dc32-ce8cb5d49733',
        'd0dd4d2b-ccf5-8b61-5c90-39f3332949c3',	'38e17df7-8250-541c-15ee-120d5a27f363',	'5d274673-f7c8-5df5-74e8-d78214a79676',
        '6c9166bf-b51d-8215-b3c1-31fcc69b550d',	'78bc62d0-8a9a-0b9b-0b9c-0ad339ef82d3',	'0dbb7871-7556-c9f4-3193-7a9cdc8707c6',
        '699f291a-9e65-c714-c855-23b646c945ad',	'f09d6b25-b818-fbd2-e561-e02f339dadff',	'd51ed1be-29e2-3838-af82-84621b1e961d',
        '760ab165-b181-1604-97ed-ebd3b814a922',	'b922ede9-c9eb-9eab-ec1c-1fecbdecb45d',	'4ad81e0e-efd6-01a7-25f6-f5fe6e5c5ea6',
        '7cc826d2-da12-57a6-09e2-c3e8d05423f9',	'69386f6b-b1df-ed68-692a-24c8686939b9',	'c861a04a-2c17-8cb3-7f12-9c0e0decf546',
        'a495eebb-fa24-3b79-c5b9-b224c482d0c2',	'44fa17cc-c2e0-a1d8-5c5e-e9b06a7ac1c6']
)
    def test_new_fields_ckp(self, uid):
        url = 'https://nir.pak-cspmz.ru/'
        url_ckp = 'https://nir.pak-cspmz.ru/cabinet/ckp/'
        loginForm = "loginForm"
        passwordForm = "passwordForm"
        username = "omg\\ealekseeva"
        password = 'KateSilver1@@'
        link = url_ckp + uid
        self.browser.get(url)
        self.browser.maximize_window()

        # Логин
        login = self.wait.until(EC.visibility_of_element_located((By.ID, loginForm)))
        login.send_keys(username)
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, passwordForm)))
        password_field.send_keys(password)
        enter = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'w-100')))
        enter.click()
        self.wait.until(EC.url_changes(url))  # Ожидание изменения URL после входа

        # Ожидание загрузки страницы и переход по ссылке
        self.browser.get(link)
        ias = self.browser.window_handles[0]

        # field_1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(2)")))
        # field_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(4)")))
        # field_3 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(6)")))
        # field_4 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(8)")))
        # field_5 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(10)")))
        # field_6 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(12)")))
        # fields = [field_1, field_2, field_3, field_4, field_5, field_6]
        # count = 0
        # for field in fields:
        #     if field.find_elements(By.XPATH, "./*"):
        #         count += 1

        # Получение полей
        fields = []
        for i in range(1, 7):  # Предполагается, что поля находятся в четных позициях
            field = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f".col-8.content div:nth-child({i * 2})")))
            fields.append(field)

        count = sum(1 for field in fields if field.find_elements(By.XPATH, "./*"))
        print(f"Количество пунктов в ИАС: {count}")

        # Переход на ЦКП-РФ
        url_ckp_rf = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.col-6:nth-child(5) div.marker.text-justify a'))).text
        self.browser.execute_script(f"window.open('{url_ckp_rf}', '_blank');")

        # Переключение на новую вкладку
        ckp_rf = self.browser.window_handles[1]
        self.browser.switch_to.window(ckp_rf)

        # Получение полей на ЦКП-РФ
        fields_ckp = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sale-detail-params")))
        field_ckp = fields_ckp.find_elements(By.XPATH, "./*")  # Ищем всех дочерних элементов
        field_ckp_count = len(field_ckp)
        print(f"Количество пунктов на ЦКП-РФ: {field_ckp_count}")

        # Сравнение результатов
        assert count == field_ckp_count, f'В ЦКП - {link} не все поля заполнены. Ожидалось {field_ckp_count}, получено {count}.'
        self.ok_fields += 1
        print("ok")

        # Закрытие вкладки и возврат на предыдущую
        self.browser.close()
        self.browser.switch_to.window(ias)
        self.wait.until(EC.visibility_of_element_located((By.ID, "topMenuUser"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".d-flex:nth-child(6)"))).click()
        exit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        exit.click()
        print(f"Проверен uid - {uid}")


class TestUsuFields:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.ok_fields = 0  # Инициализация счетчика совпадений
        self.wrong_field = 0  # Инициализация счетчика несовпадений
        yield  # Передать управление тесту
        self.browser.quit()  # Закрыть браузер после выполнения теста

    @pytest.mark.parametrize("uid", [
        'b055ca32-d55b-b34f-6b68-61c50fd2ebef',	'e2c04ce2-e678-8e0a-f77d-f5a66c5860be',	'f22e2e44-75e2-1aa3-720d-1f902ca2027b',	'47c9a94f-814c-1d1e-23cb-4fe7eb9d05fd',
        '2bb77e3b-b9a9-4269-9f15-9fa1209204fb',	'8380a7bd-69bb-bf6f-5e85-43894eec2a13',	'b2356264-3e53-74d3-9cc8-1557a172fcd8',	'35a53bd6-fef6-b592-b20f-bfbc64d3cbf3',
        '7f63bce8-935e-9d7f-7783-b5776c3a27fe',	'179519ad-c1cc-918b-7463-b748e291278c',	'b56196c0-5373-f60d-c442-e7825cd4f76e',	'22f74816-9024-cbef-bce5-c252c5f4b23d',
        '35aa8349-09ac-bc84-ddba-584d4796c0cd',	'81b07fd8-2757-f99c-390e-85ab258a85b4',	'276160bb-746d-d9d9-ad2d-9c668648ccab',	'76109291-6fb0-5420-ffa4-880a903db932',
        '3d3c965b-3e80-8292-f96c-861cc52e23a7',	'7ac6dbcd-2b41-65c9-1281-871e32b375ac',	'a3bbc216-ac11-c2fd-be6b-3403cafb58df',	'ad80a7b5-96e6-1181-1989-b17d0260ef99',
        '89c3f177-7217-8e05-d080-7a112c7a7fbc',	'ac1045e3-681a-8977-e0a1-cad77c6e3e38',	'1230740f-ffa4-fae8-bb48-2be68bc9d8ce',	'1e758e40-e997-40ba-2563-1559e9a74685',
        '5a84a7c2-82b9-a0f5-dc1e-c17aa50ffcdc',	'6158f57a-f5e3-6c6d-0877-5216a310a796',	'7002b1c3-46ba-7688-eb94-060ce2db94c9',	'2ea00e8d-95fb-71d2-a501-1f5208ff5d27',
        '0ead71a4-1e69-0bf9-9d2c-735fdf721370',	'eee31a97-6806-e21e-c93b-c66871d8a09c',	'5b879270-9afb-8a59-5b31-23bf11db249c',	'08eef663-153c-e14f-6607-62563bb9b351',
        'edc4ef5b-c4bd-63e6-81f6-c71a3ff86dfe',	'f53c2566-861c-4e1a-0869-7d3c9fa7de1d',	'eea52335-2259-c670-b942-487c1460b37b',	'3a4fb236-214f-77b0-632d-d0732a6aa0c0',
        '90474f2d-2b90-0313-320d-86156b8fb88a',	'0c9c3e38-1ac2-ceda-a4df-c1efb6e9b69c',	'b8e9541a-0249-8618-9e0c-ad7051eb982b',	'82669d1e-c412-d779-3106-9d475894e483',
        'c2cd860a-8824-329f-8649-a36a0595db83',	'2e2020eb-603e-2aca-32a2-79b04b9b2e9f',	'd614f640-a3f0-64b5-132c-2af07e233125',	'92f9f91e-a72c-f1eb-aff5-031aeaf0b9aa',
        '5d7a9e94-7429-4a44-147f-84fe09aa3f82',	'ac82654f-dbd8-9e1e-5837-cf37a28da682',	'223f9d35-252c-edba-71ab-0ce6944f0dc2',	'e0d7710b-0f2e-7f72-3ec1-479991e3d4d8',
        '7ef86fdc-45f9-e260-2d20-16f3f8c51aa7',	'b9bb9970-1f7a-0f09-6277-0a593f4371f0',	'801a746d-852b-d68a-6d75-4bfea7fd9fb3',	'0ad9418c-d28a-dd67-07dd-4854178722b5',
        '11066de2-07e6-cf55-fc03-2beaef3836b6',	'efba8d86-7609-624e-fdcd-7e7ffcbe3a68',	'ad1c02d3-e4a9-00da-8172-182351ad3491',	'abea5d87-ead6-e845-aea7-bbc7643e87bd',
        'c7d7a943-655a-5fe7-1ca9-03e13c3b2779',	'71490261-8b79-c03b-c640-7964f8f9fa82',	'e8f16b88-986f-436a-1dae-b092dafe8b10',	'd4400e02-d5cc-5b51-3644-e96dcf3d9b0e',
        'a094cb03-f888-befb-43cf-8da6cb5c74d6',	'69871c90-27f8-13d9-50b8-6bd1b8df3bbe',	'c74f9f06-5948-3fb0-91de-f16fd2eff86a',	'cf8b5204-61be-bbab-fd2b-3adb79c74e5b',
        'c0657080-de37-97e9-17f4-9af2243cca03',	'53c5e6d9-3407-0c6b-3d6d-bdb36223c77a',	'e584b015-1b2e-16b7-5830-a1ddf23c4313',	'773e4a0c-b69e-2c9c-fd5c-7e44dbc29c81',
        'fd07b45b-98ba-7ac1-4a2b-b212c2e4b7d0',	'6ee44c18-567e-996c-4d4e-c05f0cc0e798',	'6a6eb150-c570-9cf4-26c3-835c519677c4',	'cc75ea4d-8af8-7f7b-833d-7014bf74bdf3',
        'd57b0937-8980-9bbb-b5ce-9feb6d3a34bf',	'd30aacca-16a3-0607-5b4e-4aca0697a04c',	'1dc01a55-510b-a17d-df45-e41612a00338',	'ed8c3e1b-622c-a147-6c9b-cf674e156493',
        '5f01c72f-4234-0c87-e074-fba27e8382fe',	'5d452f2c-6d9c-bcad-a80d-c423d69c33ff',	'0f841800-d17c-84f1-2859-1cc1fedde905',	'a6b046b2-6232-b6d5-d26b-f0c1a563cfd4',
        '653c827e-82e8-d9fa-77d1-49b020aba765',	'4e4d8bf9-15ba-c658-7f46-3c95f45dffa7',	'd6a388ed-7f5a-a807-0eec-fce35f5076f5',	'4fc9c47b-f817-c732-f4c0-0923fe2bce9c',
        '9076b975-4383-6a67-83e0-c8625d647fe1',	'93295df6-dd0f-83ef-6ad0-326e7353cdbd',	'2ec606db-6b63-5960-5d6f-27b2587a80ea',	'e484924a-e85e-d1a1-da06-84887b076877',
        '08c4de0a-d18c-abf4-4bec-21692b7ae7f3',	'8366af8b-ee91-0925-9b6d-fd87bc4fe51e',	'bf87cacd-9060-37e5-ea03-4d8bddf7ff70',	'804603a5-f629-7c07-e039-cd9ec189cbe4',
        'af896ed8-ff5e-3bcc-ea22-8a8b911d79cd',	'8d001905-e352-9e30-4362-cab7dd57c941',	'c054b638-fb56-bec8-213c-5242fcfb31e7',	'ce3db407-b86f-8d19-2ac4-0250d0b67d5e',
        'e63433a7-4489-2960-e364-5c61f5670c4a',	'035cbdf4-581e-e4c1-cf02-71a6e82d46dc',	'bde79bbf-002a-d088-a4e5-97fa11e1aa6d',	'd1b48e98-d686-72e4-eb9b-8a8b06799ede',
        '862934a3-ccd6-2f0a-6b96-131c558a2c47',	'ec14ca89-6aaa-c90d-6a0f-e03d8e3c68f8',	'90763e2e-68f4-1077-55a0-f9881d5c4f47',	'f44887d4-c83c-9628-f0e9-140ee3f0bff7',
        '82b4f1d7-eb9d-cfb9-a4fb-70cff789ad2e',	'80f4fac7-96ab-5fe3-b2e3-db87cd3e9246',	'8c25826a-98be-6311-db30-de16254cc578',	'5d0d9722-9c5c-4d80-1eff-2ffc8412243f',
        '877fd7a6-7c6e-d4c8-3ff6-163ba73896c0',	'a8216f2c-960a-8a49-23b7-8c36db6d2488',	'a6c5ef06-8162-0ad0-93de-3a53eba6b9df',	'a4ee149b-b2c0-c91e-6059-4864e9fef0c2',
        '913ddba5-57db-7780-ff40-23fb4cb29062',	'c7824a18-2ab4-abc5-fcd7-e6a443b73f0d',	'b1643bfe-c2a7-870d-164f-c70e33fb9367',	'986b0ac8-43b6-9095-22bd-6d10b1f2e2d0',
        '610dba3b-8de3-aece-92a7-dff8b15e82d8',	'8a39b68e-7dad-d525-3cc6-65be50a164ca',	'9e33f592-ddfb-6e25-3413-68b76acd4816',	'a3230b75-7801-0ae8-c8cd-6867ecd37701',
        '9ebbdbb8-4f37-95d5-4631-abcdfe772fbd',	'37ef41c2-510a-3531-4b7d-eb1b5b167e8f',	'1eaf209b-8e7e-12ec-fe0e-cef3eedc166a',	'b354048e-7c68-002f-74ee-7546c66b3a9d',
        'ce910672-7d23-af70-99c3-6f571fceb294',	'e406d57a-ec43-72bc-7c2c-aded28f15bb4',	'42de165f-aa6d-598d-cb8e-e5b280900a7a',	'd67bc4fb-2c59-e40b-db36-8ed3b0b07e63',
        'd854234c-f1f2-6b77-b259-a8511912040b',	'a498064a-de78-6ab4-9115-a6db2690f2b8',	'be8bfda1-bbe0-bf5c-cc0f-46676b3c8cd0',	'c6087c63-2574-0286-128d-ef0c490b7ac6',
        '7781ada7-3e38-3da9-ef95-5eb94373f08a',	'25590102-d65a-90ba-43eb-bc1a72b0f2f9',	'86e4ff8c-c268-ab36-c7e3-c5c53d2293a4',	'63376d36-5d6c-cac7-3bac-234517e0bb42',
        '222593a8-102a-0c14-12e8-c60cbf331aa9',	'b929cd8e-b0cd-508a-acce-86a54d7a55dc',	'5d222ae7-af1c-2621-82cd-38673b51f6aa',	'350cc9ef-4b66-3635-54d5-ee36b3501088',
        '2e988375-5e10-a325-332a-a58bacf0dff6',	'd531a4e4-9e3b-bfea-6e7a-b955afaf2c53',	'd9ca83a5-8c83-3c5f-549c-1da97d5f9ed6',	'203e61ab-9cbc-64ec-8cdb-39fbeb0ed80e',
        '98cf16f5-ab6f-ead8-0695-78fddcc6536d',	'4c19391d-894b-a5f7-beda-84353628644d',	'044e2bfb-f3fb-9f1a-69f2-ba8395f74fb7',	'28265fb6-720d-c73f-e191-c77deaba7d97',
        'ff2c51e3-7719-0d5c-6b8f-d60874c8c4e2',	'6f30bc90-f5fd-35df-81f2-31d354c3798f',	'5d4e3c13-1990-0734-ed91-15dce48cc6e2',	'13fcce20-9691-b929-763f-246063b67d5b',
        '45ad7dd0-bdf3-cbe6-19f7-0a1549288826',	'6282253a-5484-fc82-4ff4-56ccaa4a140b',	'1a19eb0a-5355-e070-f37b-12b0690bc670',	'89a87090-a3d1-24a1-9457-09ce91485377',
        '5f01f6ba-9be5-a4fe-be11-a06a9bf05dfc',	'74b3b02c-0bb7-d3a3-0f67-882c3c64ff6a',	'bdcc96b4-f7c6-0e97-9b48-409477d35294',	'be456218-7583-eab0-7c46-b6bc637248cd',
        'e6da0a1b-52de-51a1-afba-f4ffd410809e',	'70a4710d-7afc-d39f-225e-5f311643eb9f',	'cd530fd8-e90b-49ce-9b55-ebb0b2be5e96',	'f9402744-c93f-b239-fc49-fc2f383a12cc',
        '7ab7ea40-792d-b3bc-e9fa-b198e266b7d1',	'c20b9ac3-6b6a-a735-d724-2c106cf1d098',	'5eb562fe-4009-a9fa-998c-64505f648a87',	'8a12ce50-6d46-5a58-9687-2b695030b34d',
        'f4355c09-1225-774f-35ef-3cb25c1e2b6b',	'11b97514-78fa-8741-d493-5017eeb51b04',	'abac74db-42a9-91c4-9627-fe2c13ac3254',	'4844688d-fa47-3d25-aeda-9810b09585d3',
        'e5d8973a-e435-ab52-c759-2094dada817e',	'49a2be29-ab49-77d1-1ce5-10b2810c3fdb',	'27a24dd4-1b85-0c94-3375-29f9ceb2bd34',	'223d12e0-9b91-0b2c-61d8-697749358318',
        '1fa448ee-ccd7-8987-ad24-ba58261f82ad',	'8acb5376-7dea-843f-002e-1d628cb223fe',	'4033fedf-f2cb-16df-8cbf-1a4d4c8ef98a',	'36be5aa4-26e2-4c1f-0c48-baa196569fdd',
        'f1eb5849-fc68-91eb-25d6-94daf60ca97b',	'5e9712c2-e8e2-7f71-cdd5-fdbc443448b0',	'cfb527c5-2cef-da0f-bd3a-54c477355617',	'7c018a6e-5920-d19a-6ab8-327dc3014a3c',
        '52742a60-4b9e-59ae-8959-d80acfcb17b5',	'78f16922-2b13-7180-7681-b71c3569b0e4',	'2c33e251-5702-29bc-5cc0-1977cb31607b',	'c489b935-5232-adea-4b31-1444156b5926',
        '5774ee3d-4662-68a5-3bb1-06f7af7b14b4',	'848cd27a-a495-f946-0b87-124534aa5d47',	'55eec28a-61e3-9afa-2bf9-13e969b5685e',	'df40cc02-9a2a-20e8-620e-4d64fd3869bb',
        'd5480de5-9a07-776f-b247-766348df9674',	'a4e2667b-e0e0-8ff0-b20a-0e840d10ab64',	'eda7687a-f9fd-e191-4d9e-85a733426452',	'3d23a2d7-b036-dc73-39d5-0db02be55e5b',
        'dc66c1b1-d0f0-985c-5547-c348a40db34e',	'e9cd0062-c385-58b6-b5da-47528a898b0a',	'33fa2d27-2cb6-7c9e-3456-5e514b481150',	'f6394b5c-d7fa-99cf-2ee2-28794dc9abe3',
        'a7abf4d2-6c0d-c6a8-cce1-400824b48f01',	'cd04dd42-dc7e-0bce-9cf4-91bb0e5f9a8c',	'd7e0596c-30e1-c30b-7444-59d5898ac038',	'22bb2b55-abe9-5131-aa6d-423f7de224b2',
        'f60b71a8-4544-3d27-38de-a590a56869d9',	'9da7a746-191a-c8a8-f548-80bebebfebd8',	'63895f0d-9a7b-a1b4-3f4b-cdcaf0201c01',	'1f3f1e09-5c95-ebe1-9576-761d1d50fd62',
        'a3c63214-3f46-a1d2-01fa-de2ec3ac1a1d',	'b99d4a02-aad6-cef5-dac3-3da6b0043526',	'02b115b7-2e63-0661-8b6e-3e08bc8489b2',	'dcf0e000-590e-b249-91d2-debe745b1b9d',
        '7b1022cb-05e2-9e19-7ef0-32da42910a30',	'8304712e-d2a0-233f-3f61-2572f70dca29',	'f8a74c1e-a8b7-3146-a5c2-f5b597e313d6',	'93be52ba-8f82-8a41-647f-919a5b646221',
        '1819f733-e30e-4273-71b7-cb5a99ca2982',	'e747ed3c-23f7-de98-947c-b140a1bd1a22',	'a785ead0-4130-69ba-7507-74f78bafbd83',	'd4166ff7-5ac2-db73-e0c4-e1b1212f51d1',
        '72ac44be-87f4-f1a6-9769-d73a96bc09ff',	'20a1acce-6233-dd78-a02d-484e97f6760e',	'1bac4230-de5e-db66-151d-b8598c1eef36',	'fe275b97-5c66-660e-a501-7b327e3fc2e7',
        '3440f0cb-3831-1aad-9a05-111ce8c4e582',	'd64086da-e876-b680-116b-9ee2e16795db',	'531b5f6e-61d8-b957-69cd-34dfa3b85c2b',	'752e863c-be3b-d364-2d9a-a98891db0df6',
        '8ed523b9-d5f0-9cd6-771d-44fe043ea6b8',	'75d28a2a-89ac-b305-d193-0e4d4cdbce5a',	'5c2def0e-f886-5f33-a3eb-28a5a64c2bb9',	'b03e8d29-44a5-3322-18c7-3687073ec0fd',
        '3df2c34c-e72a-d870-836a-1b8d33efb8ab',	'c74d5b63-20f8-5b58-77d0-c1f1ccedfe67',	'78a58a39-2357-3676-12b4-75f8955990cb',	'bef3e1c6-a539-c44f-b3ff-67d400a31861',
        'b13fb938-3539-48c2-e38c-3acdc6f1db4d',	'72619de5-29d5-1a1c-7696-0732b1d4ecd9',	'f7dde564-7e64-f79b-30fd-1844ddaaea68',	'8fad1c35-4258-e212-aec9-340ede0aae8a',
        '7fdf78b9-d975-00ba-fa47-74771b6968ca',	'123468c6-9db6-050d-42c8-c75ff798061c',	'f4d5efd6-c5fe-dddb-c26a-e4517d610428',	'c9d467ff-9689-8afb-1101-114847e00092',
        '7b9eab9b-966b-ef72-f88d-2dad64d5d1e0',	'011707fd-64ad-1ebe-a42a-17ab71cb12bd',	'cbe41f0c-3c73-b890-35e6-fa112456b80b',	'daff10c8-dccf-b1b8-3a48-f1ff6f9f9b13',
        '3ddf6762-d248-7bd2-3093-ddd1dbf0dd56',	'7033391e-a515-9b02-b6e9-8cc32fa4fa52',	'5989cf2b-020a-32e4-546f-8f1dfa2f3aaf',	'badd7c6d-7357-9b9a-acb5-30c257edf04e',
        'f4a4e24e-b8ff-534f-7a6a-cbe756cf2f65',	'8bee9635-fcd7-1db9-4f48-ce05bb0270e6',	'b37f6ff7-029b-365b-5c6f-15eb27fe7d6f',	'8f1715c6-5749-e0f9-55ee-26bdb4233ef3',
        '974a0eed-5e3e-4463-d914-072efbd66e16',	'b8f6fff8-acb6-884f-a1b7-5987fed24bbc',	'b75698f2-843f-f7cb-fe1f-6dde0b43c1ba',	'84947fc9-70cf-8fc4-4192-c5c5e6385e6e',
        'fa44f45c-be3c-f2a4-4f43-301d3702e15d',	'e079292e-7644-5d6b-1664-ab53e0106743',	'0076a885-8e3c-9c33-79f1-35b071637d49',	'3c36dd94-86f6-829f-0efa-afe020901ecd',
        'c9858368-ce8a-7176-e01f-52eb4e72e7b3',	'e7ac16f6-58ec-3a58-d5a7-d54094c4a034',	'd8a93979-a0d1-cc26-5c69-042d40021e50',	'052b601a-ea98-9d07-6b62-909bd7ef3102',
        'ebbaaffc-6377-2b89-e488-c5233d8b9fd4',	'e20a3f87-6a16-d249-77ad-6f5ee5660a2b',	'd5f72cd1-3c19-6267-5722-17816a201c69',	'36e3008b-a6f6-d7fc-64dd-caaea5299fec',
        '06edb348-3e70-e5ed-5ceb-56a070983ce1',	'bba5abab-6178-5994-94ae-676d92f41f9d',	'1764c10d-d219-f07a-2b87-460f4e6b4a55',	'8ec0888a-5b04-139b-e0df-e942c7eb4199',
        '34ca67a0-5cbc-9d94-4617-8fd278d06625',	'00829d6c-843a-aad2-38a0-7e263bc5e424',	'1d775b30-2ed7-85cf-ff57-bc104cccc3f8',	'5e8625c1-b3f8-266c-4679-8ef0f074b960',
        '5c421fd6-3a9c-265a-65d8-b184265648f7',	'b6a1cb5c-6794-f163-0034-183f98b2136b',	'0854af59-08f6-9786-bcf4-78142222082c',	'10ba54a7-e46c-2f39-1930-527275f8c231',
        '6b440f5e-2141-3035-5a39-30974c290fbe',	'9266ac5b-e4f2-b8e1-ec42-9dafa3d895de',	'27ffa859-13c6-3775-2a01-e0b44572462d',	'b3c0b332-ea87-34da-e04d-e7548ad18851',
        '5b6b1526-e38d-e793-08ca-d745b342b87e',	'f7017cf1-c449-0e1a-42fd-5a43a227b086',	'd76a7db8-ab51-00e4-9416-b520c2d2b9d7',	'a70ae7b9-ac32-d7cb-1b26-8a1900e46857',
        '22f4ed35-f971-a18a-0fcb-ee765d02d963',	'd4832109-dedf-29b4-43ac-0534c31bef75',	'40815ed8-dd01-9756-2c66-2e33330f54a6',	'8cdd2b02-a32a-dc1a-5e44-98acfb639ddb',
        '00160b61-7682-32a7-3be6-a70c6bff3771',	'ebaa1326-449e-70aa-2b56-03397e48383a',	'fe41bea4-d634-65e8-04af-e22ae01a660c',	'aefa054c-968f-7d0b-480d-b2cd848044cc',
        'ad09e45e-cf36-2ff5-829f-e29771bee9ac',	'84c8cac3-9d56-81c7-1451-c34fe0197991',	'3354a3dd-6bb5-9d16-f5d9-835a0d78e160',	'3fc8879e-3b33-321e-430a-e72d7ab8fc9b',
        '8753cbf3-507b-1ae9-d562-f9b2bbc0d1eb',	'79f25363-8d58-ed40-f15c-2c6d4d4c1238',	'ad8b922f-fc4c-7dfe-244c-4f2b063d09b3',	'6bb9b198-8302-afae-939a-f147c690ef4d',
        '0ca6926a-50ad-07b6-47da-dee884e84c7f',	'bc85695f-2e5b-204b-23da-ed4988391787',	'94159ff9-9515-9420-f80b-6ca02937d345',	'd899e4f8-1128-32f4-84de-338cafe88d76',
        'cd26cf71-d0ee-d5d9-94b6-9664eb12aaed',	'a2b8c811-480b-e931-8ee6-09450fc0c237',	'5e55c8cb-136f-f338-0792-5e533310b206',	'a7d6ec26-3654-2b97-1de4-9d71e972243e',
        'fb2f8fcc-928d-44e0-deb3-3591b727df88',	'e9823930-ddd2-5303-2504-c67984ff83dd',	'cd62dca1-76af-fcf6-a298-93a044fc7f19',	'7d560c6d-8b7d-62a3-5c04-f4d1a7c7099b',
        '1c79085f-6634-0d8b-e06a-09cfd2eb4f11',	'07a7e4f2-47a3-7d0a-0e89-8b2f49ad78ef',	'70c89761-9faa-59cd-40cc-270dc64c0e01',	'177b6f6f-ecc5-0e98-8a65-e0a97a9f8900',
        '1d29780f-f644-d35c-8e06-e07747c82dd8',	'787c50e0-c695-4bf8-01bb-7390c2fd292f',	'ca344476-de21-ce19-3974-14fd42a9d131',	'57308eff-c536-64f7-9d81-78e4d8201bc8',
        '1083c5e1-2e24-b420-3d80-51aa21676b9c',	'6d237d68-8717-7de9-6235-bd0b62c5d081',	'66c42448-411e-d523-db8b-dbfe1ec92189',	'7abb96ac-66bf-38c2-1b72-9cb062ecb0b3',
        'a8851efe-c726-7e09-caec-f8ef3a094f50',	'ece68e2b-d08d-e2b4-20f3-cabb209b1a16',	'bd4ce68d-ec3b-986b-ee61-5b146be18299',	'a6c2a07e-4bd5-f450-5976-9e9ff9d42ea2',
        'dae3e8d0-12db-89b6-fd0d-f2e413bd18da',	'84e8a56d-4bed-d1c9-0a84-21e4ead9e9fb',	'a2fe006f-f242-d17a-3135-a35416588d43',	'ed69dd69-2309-0854-240e-4c08e2cf0228',
        '35dc50a0-c808-ac73-bd72-37d6e24d753e',	'254cac17-234a-29b6-7717-3d1d17130503',	'f2f8a7bd-438d-b226-f6e1-80190cb668f3',	'5e0ffe61-78b1-9737-daf4-28c27d1a23a6',
        'cb2dae0c-baf0-6c40-cfe2-64ad37f56da8',	'cd65feca-0a7f-c838-e875-30293ac51a5f',	'ab2db16c-097a-f382-bb56-30e3ace15101',	'0fcae286-bc73-2eb1-e660-1c1a0aeedf0a',
        'f6dfd431-b9be-0d77-2a03-7e36dccf19b8',	'083973a6-3471-d05b-ea02-09cf7249ff4d',	'093ad23f-3867-4bdb-6087-2947d862b942',	'81272c14-a9e3-daed-f0d5-6c926ef55799',
        '3e795844-e92b-5402-9c40-f3ff3af28792',	'90c81017-c007-9335-5d87-9732987e5c0a',	'2c4ef56c-69ca-af94-722c-40974783d9af',	'e177e521-bb05-f46e-eb59-07d8c05b34af',
        '051442a9-a65c-971b-e60f-3128d1c98632',	'04ba9070-9cfb-4418-5a22-e6e119a5bdb5',	'72f15862-c7cc-706c-42c4-2c4b2f8ce41e',	'bc5ac473-c968-2dce-0386-4c0124a5dbcd',
        '109c7495-cacb-dc53-cc2e-b1e835efcfba',	'28f51206-53a8-a33c-e1d5-acc2bcc000d5',	'7bc21300-5c31-9976-4753-45f912211bd0',	'2c7c65a8-4313-afa0-431a-fb1dadf588e6',
        'f51a1012-cc29-b571-04ee-938da9fefb3b',	'265b8f84-f825-abc3-4eb6-807a3bbb2a32',	'357a42fe-2302-1428-2090-422e27f7cc5a',	'b89fb546-4e04-efe4-dfae-689358d5a06f',
        '1473efb3-59db-ca0e-9224-055ab06d96d3',	'b4fdcf75-973f-9365-2032-73bac263b332',	'de61523e-ea0e-3dd1-1cb8-aff0d761ddc2',	'd5aa6a21-fa97-89dc-40f9-ca186ac254f2',
        'e196a996-9474-bd61-a138-dcd66371297d',	'e50303e2-ea08-7704-d729-e171045b7ec4',	'6969328a-218f-f4f9-39b5-e8bcb81f7bac',	'67fbfc2d-7add-1091-684f-0e79a2e06035',
        'f9f18975-dadc-cc86-c848-5f566a70e4db',	'56502826-a9a6-5c49-1637-639a70fbe57b',	'5e037904-f069-d5d0-9830-083f3243ec9f',	'6ce20ae0-4939-2e8d-6e94-4c9e49f8e024',
        '3cbeb962-8aef-c214-5acc-691efc119fd7',	'a2a6e2d6-5ff6-7c5e-d23a-2d6cd3beb666',	'3703f670-b0f0-18ec-eca0-3c233324be34',	'4aa43b38-171a-a5cb-4d58-2ccad86709ac',
        'a6ea4f70-bb6e-239b-e7fe-d07dbf37cb7d',	'bbb4a9e2-bbf0-1de9-0ee9-335cec9a2c5e',	'e7ef57d1-89a8-108f-cc58-0fc2c6129f1c',	'7b0af45b-f4a5-dc2e-155a-6fec8966f5c7',
        '6205a3c6-bd39-1523-c2eb-6cdb55d7653a',	'fd219711-ca5c-b0be-6e31-fda862530d19']
)
    def test_new_fields_usu(self, uid):
        url = 'https://nir.pak-cspmz.ru/'
        url_usu = 'https://nir.pak-cspmz.ru/cabinet/usu/'
        loginForm = "loginForm"
        passwordForm = "passwordForm"
        username = "omg\\ealekseeva"
        password = 'KateSilver1@@'
        link = url_usu + uid
        self.browser.get(url)
        self.browser.maximize_window()

        # Логин
        login = self.wait.until(EC.visibility_of_element_located((By.ID, loginForm)))
        login.send_keys(username)
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, passwordForm)))
        password_field.send_keys(password)
        enter = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'w-100')))
        enter.click()
        self.wait.until(EC.url_changes(url))  # Ожидание изменения URL после входа

        # Ожидание загрузки страницы и переход по ссылке
        self.browser.get(link)
        ias = self.browser.window_handles[0]

        # field_1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(2)")))
        # field_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(4)")))
        # field_3 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(6)")))
        # field_4 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(8)")))
        # field_5 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(10)")))
        # field_6 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-8.content div:nth-child(12)")))
        # fields = [field_1, field_2, field_3, field_4, field_5, field_6]
        # count = 0
        # for field in fields:
        #     if field.find_elements(By.XPATH, "./*"):
        #         count += 1

        # Получение полей
        fields = []
        for i in range(1, 9):  # Предполагается, что поля находятся в четных позициях
            field = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f".col-8.content div:nth-child({i * 2})")))
            fields.append(field)
        count = sum(1 for field in fields if field.find_elements(By.XPATH, "./*"))
        print(f"Количество пунктов в ИАС: {count}")

        # Переход на ЦКП-РФ
        usu_rf = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ms-2 .ms-1')))
        url_usu_rf = usu_rf.get_attribute('href')
        self.browser.execute_script(f"window.open('{url_usu_rf}', '_blank');")

        # Переключение на новую вкладку
        usu_rf = self.browser.window_handles[1]
        self.browser.switch_to.window(usu_rf)

        # Получение полей на ЦКП-РФ
        fields_usu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sale-detail-params")))
        field_usu = fields_usu.find_elements(By.XPATH, "./*")  # Ищем всех дочерних элементов
        field_usu_count = len(field_usu)
        print(f"Количество пунктов на ЦКП-РФ: {field_usu_count}")

        # Сравнение результатов
        assert count == field_usu_count, f'В ЦКП - {link} не все поля заполнены. Ожидалось {field_usu_count}, получено {count}.'
        self.ok_fields += 1
        print("ok")

        # Закрытие вкладки и возврат на предыдущую
        self.browser.close()
        self.browser.switch_to.window(ias)
        self.wait.until(EC.visibility_of_element_located((By.ID, "topMenuUser"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".d-flex:nth-child(6)"))).click()
        exit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-confirm")))
        exit.click()
        print(f"Проверен uid - {uid}")
