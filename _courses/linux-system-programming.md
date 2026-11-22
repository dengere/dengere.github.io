---
title: "Sistem Programlama (Linux & POSIX)"
summary: "Linux çekirdek sistem çağrıları, süreç yönetimi, çoklu iş parçacığı (POSIX threads), süreçler arası iletişim (IPC) ve ağ programlama temelleri."
type: "course"
categories:
  - "Sistem Programlama"
  - "C / C++"
order: 2
sample: true
instructor: "Kaan Aslan"
start_date: 2026-12-12
schedule: "Hafta Sonu (Cumartesi - Pazar 14:30 - 18:30)"
format: "Online"
duration: "120 saat"
---

## Kurs Hakkında

Bu eğitimde POSIX standartları ve Linux işletim sistemi mimarisi üzerinde doğrudan sistem çağrıları (system calls) kullanılarak düşük seviyeli uygulama geliştirme teknikleri ele alınır.

## Kurs İçeriği

### Dosya Sistemi ve G/Ç İşlemleri
* Düşük seviyeli dosya tanımlayıcıları (`open`, `read`, `write`, `lseek`)
* Dosya kilitleme mekanizmaları ve bellek eşlemeli dosyalar (`mmap`)

### Süreç ve İş Parçacığı Yönetimi
* Süreç oluşturma ve yaşam döngüsü (`fork`, `exec`, `wait`)
* POSIX Threads (`pthread`) ile eşzamanlılık ve senkronizasyon (`mutex`, `semaphore`, `condition variable`)

### Süreçler Arası İletişim (IPC) ve Ağ Programlama
* İsimsiz ve isimli borular (`pipe`, `FIFO`), paylaşılan bellek (`shared memory`) ve mesaj kuyrukları
* Soket programlama temelleri (TCP/UDP istemci-sunucu mimarisi)