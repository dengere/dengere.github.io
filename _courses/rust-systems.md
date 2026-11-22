---
title: "Rust ile Sistem Programlama"
summary: "Çöp toplayıcı (garbage collector) olmadan derleme zamanında bellek güvenliği sağlayan Rust dilinin sahiplik modeli, eşzamanlılık ve sistem programlama pratikleri."
type: "course"
categories:
  - "Sistem Programlama"
  - "Modern Sistem Dilleri"
order:
sample: true
instructor: "Kaan Aslan"
start_date:
schedule: "Hafta Sonu (Pazar 10:00 - 14:00)"
format: "Online"
duration: "96 saat"
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