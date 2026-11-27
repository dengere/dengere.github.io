---
layout: course
title: "C Programlama Dili (Test 2)"
summary: "C programlama dilinin tüm sentaks ve semantik yapısını kapsayan temel eğitim."
categories:
  - "Temel Programlama ve Bilgisayar Bilimleri"
  - "C ve C++ Programlama"
order: 2
duration: "240 saat"
instructors:
  - "Kaan Aslan"

sessions:
  - start_date: 2026-12-14
    schedule:
      - "Salı 19:30 - 22:30"
      - "Perşembe 19:30 - 22:30"
    instructor: "Necati Ergin"
    note: "Hafta içi akşam grubu (Çevrimiçi)"

  - start_date: 2027-01-16
    schedule:
      - "Cumartesi 10:00 - 14:00"
      - "Pazar 10:00 - 14:00"
    instructor: "Kaan Aslan"
    note: "Hafta sonu grubu (Mecidiyeköy Şube)"
---

## Kurs Hakkında

Sistem seviyesinde yüksek performans ve bellek güvenliğini bir arada sunan Rust dilinin temel yapı taşları, ödünç alma denetleyicisi (borrow checker) ve C/C++ ekosistemleriyle birlikte çalışabilirliği (FFI) ele alınır.

## Kurs İçeriği

### Sahiplik ve Bellek Güvenliği Modeli
* Ownership (sahiplik), Borrowing (ödünç alma) ve Lifetimes (yaşam süreleri)
* `Option`, `Result` türleri ve hataya dayanıklı yazılım geliştirme

### Soyutlama ve Eşzamanlılık
* Trait sistemi, genelleyici türler ve sıfır maliyetli soyutlamalar (zero-cost abstractions)
* Veri yarışlarını (data race) derleme zamanında engelleyen çoklu iş parçacığı programlama

### Sistem Seviyesi Uygulamalar ve FFI
* `unsafe` bloklarının sınırları ve ham işaretçiler (raw pointers)
* C kütüphaneleri ile etkileşim (Foreign Function Interface) ve gömülü/sistem araçları geliştirme