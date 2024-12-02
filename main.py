from abc import ABC, abstractmethod

class AnalyticsProvider(ABC):

    @abstractmethod
    def get_visitor_stats(self):
        pass

    @abstractmethod
    def get_traffic_sources(self):
        pass

    @abstractmethod
    def get_conversion_rates(self):
        pass


class GoogleAnalyticsProvider(AnalyticsProvider):

    def get_visitor_stats(self):
        return "Статистика по посетителям из Google Analytics"

    def get_traffic_sources(self):
        return "Источники трафика из Google Analytics"

    def get_conversion_rates(self):
        return "Показатели конверсии из Google Analytics"


class YandexMetrikaProvider(AnalyticsProvider):

    def get_visitor_stats(self):
        return "Статистика по посетителям из Yandex.Metrika"

    def get_traffic_sources(self):
        return "Источники трафика из Yandex.Metrika"

    def get_conversion_rates(self):
        return "Показатели конверсии из Yandex.Metrika"


class AnalyticsReport(ABC):
    """Абстрактный класс для отчетов."""

    @abstractmethod
    def generate_report(self, provider: AnalyticsProvider):
        """Создание отчета с использованием данных из провайдера."""
        pass


class WebAppReport(AnalyticsReport):
    """Отчет для веб-приложения."""

    def generate_report(self, provider: AnalyticsProvider):
        """Создание отчета для веб-приложения."""
        visitor_stats = provider.get_visitor_stats()
        traffic_sources = provider.get_traffic_sources()
        conversion_rates = provider.get_conversion_rates()

        report = f"Отчет для веб-приложения:\n" \
                 f"Статистика по посетителям: {visitor_stats}\n" \
                 f"Источники трафика: {traffic_sources}\n" \
                 f"Показатели конверсии: {conversion_rates}"
        return report


class MobileAppReport(AnalyticsReport):
    """Отчет для мобильного приложения."""

    def generate_report(self, provider: AnalyticsProvider):
        """Создание отчета для мобильного приложения."""
        visitor_stats = provider.get_visitor_stats()
        traffic_sources = provider.get_traffic_sources()
        conversion_rates = provider.get_conversion_rates()

        report = f"Отчет для мобильного приложения:\n" \
                 f"Статистика по посетителям: {visitor_stats}\n" \
                 f"Источники трафика: {traffic_sources}\n" \
                 f"Показатели конверсии: {conversion_rates}"
        return report


google_analytics_provider = GoogleAnalyticsProvider()
yandex_metrika_provider = YandexMetrikaProvider()

web_app_report = WebAppReport()
mobile_app_report = MobileAppReport()

web_app_report_google = web_app_report.generate_report(google_analytics_provider)
print(web_app_report_google)

mobile_app_report_yandex = mobile_app_report.generate_report(yandex_metrika_provider)
print(mobile_app_report_yandex)