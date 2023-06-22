import re
text = """3
ФОРМА
Директору федерального государственного бюджетного учреждения «Российский детско-
юношеский центр», 119048, г. Москва, ул. Усачева, д. 64.
Директору федерального государственного бюджетного образовательного учреждения
дополнительного образования «Федеральный центр дополнительного образования и организации
отдыха и оздоровления детей», 107014, Москва, Ростокинский проезд, д. 3.
ВрИО директора федерального государственного бюджетного образовательного учреждения
«Всероссийский детский центр «Океан», 690108, Приморский край, г. Владивосток,
ул. Артековская, д. 10.
от __________________________________________________________________________________,
проживающего по адресу ______________________________________________________________ ,
паспорт серии ___________ No __________________________________________________________,
выдан _______________________________________________________________________________,
дата выдачи __________________________________________________________________________,
код подразделения ____________________________________________________________________.
Согласие на обработку персональных данных (для участника)
Я, ____________________________________________________________________________ ,
являюсь участником конкурсного отбора на участие в дополнительной общеразвивающей
программе «Всероссийский чемпионат по программированию «Цифровые старты» (далее –
Конкурс), проводимого федеральным государственным бюджетным учреждением «Российский
детско-юношеский центр» (119048, г. Москва, ул. Усачева, д. 64, ОГРН: 1167746501064, ИНН:
7703410980), федеральным государственным бюджетным образовательным учреждением
дополнительного образования «Федеральный центр дополнительного образования и организации
отдыха и оздоровления детей» (107014, Москва, Ростокинский проезд, д. 3., ОГРН: 1037718018447,
ИНН: 7718244775) в партнерстве с государственным бюджетным образовательным учреждением
«Всероссийский детский центр «Океан» (690108, Приморский край, г. Владивосток,
ул. Артековская, д. 10, ОГРН: 1022502127592, ИНН: 2539009984) (далее по тексту именуемые
«Организации»), в соответствии с требованиями ст. 9 Федерального закона от 27.07.2006 No 152-ФЗ
«О персональных данных» даю свое согласие Организациям
на обработку моих персональных данных с целью моего участия в Конкурсе, которое проводится
в 2023 году.
В указанных выше целях Организации в установленном действующим законодательством
Российской Федерации порядке имеют право поручать совершение отдельных действий
с персональными данными третьим лицам при условии, что они обязуются обеспечить безопасность
персональных данных при их обработке и предотвращение разглашения персональных данных.
При этом такие третьи лица имеют право осуществлять действия (операции) с персональными
данными, аналогичные действиям, которые вправе осуществлять Организации.
Перечень моих персональных данных, передаваемых Организациям на обработку: фамилия,
имя и отчество, серия и номер документа, удостоверяющего личность (паспорт), сведения о выдаче
документа, удостоверяющего личность (включая дату выдачи и код подразделения), адрес
регистрации по месту жительства, дата рождения, сведения о месте фактического проживания,
4
сведения о месте моей учебы, адрес электронной почты, номер телефона, видео- и фотоизображения
(в том числе на электронных носителях информации).
Я даю согласие на обработку Организациями моих персональных данных (в том числе,
на совершение следующих действий: сбор, систематизацию, накопление, хранение, уточнение
(обновление, изменение), использование, обезличивание, блокирование, уничтожение
персональных данных), а также на передачу такой информации третьим лицам в случаях,
установленных нормативными документами вышестоящих органов и действующим
законодательством Российской Федерации.
Настоящее согласие действует до достижения целей обработки либо до моего отзыва.
Настоящее согласие может быть мной отозвано в любой момент путем направления
соответствующего письменного заявления на адрес электронной почты: info@rdcentr.ru, или
по адресу: 119048, г. Москва, ул. Усачева, д. 64. Я уведомлен(а), что Организации вправе
продолжить обработку персональных данных в случаях, предусмотренных действующим
законодательством Российской Федерации.
Я по письменному запросу имею право на получение информации, касающейся обработки
моих и моего ребенка персональных данных (в соответствии со ст. 14 Федерального закона
от 27.07.2006 No 152-ФЗ «О персональных данных»).
Подтверждаю, что ознакомлен(а) с положениями Федерального закона от 27.07.2006 No 152-
ФЗ «О персональных данных», права и обязанности в области защиты персональных данных мне
разъяснен"""
# match начало строки
# search до первого совпадения
# findall ищет везде
match = re.findall(r'[a-zа-яё]+', text, flags=re.IGNORECASE)
print(match)