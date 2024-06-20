---
draft: true
date: 2024-06-20
categories:
  - xiaohongshu
  ---
  
# Linux释放磁盘空间

## 步骤

- **查看磁盘空间使用情况**: `sudo du -cksh * | sort -hr`，这个命令可以列出当前目录下每个文件和子目录所用空间大小，并从大到小排序。通过多次使用该命令，可以探测到使用空间最大的文件或目录。
- **释放磁盘空间**: 
	- **删除文件或目录** :`rm -rf [file name or folder name]`，这个命令可以循环删除指定目录下的所有文件和子目录。
	- **删除不使用的软件包**:`sudo apt autoremove` or `sudo apt remove [package1] [package2]`
	- **释放apt缓存**:`sudo apt clean`
	- **删除系统日志**:`sudo journalctl --vacuum-time=3d`，这个命令会删除所有3天前的系统日志。

> 记录一点一滴，笨人的平凡生活